import concurrent
import time
from concurrent.futures import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


def fetch_and_parse(url, browser):
    response = requests.get(url)
    #time.sleep(2)  # Wait for JavaScript to render the page
    soup = BeautifulSoup(response.text, 'html.parser')
    answer_div = soup.find('div', class_='s-la-faq-answer-body')
    if answer_div:
        return answer_div.text.strip()
    else:
        return "Answer not found."


def parse_answers_from_urls(faq_list, browser):
    with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
        future_to_url = {executor.submit(fetch_and_parse, question['url'], browser): question for question in faq_list}
        for future in concurrent.futures.as_completed(future_to_url):
            question = future_to_url[future]
            try:
                question['answer'] = future.result()
                print(f"Answer: {question['answer']}\n")
            except Exception as exc:
                print(f"{question['url']} generated an exception: {exc}")
    return faq_list


def preprocess_browser():
    chromedriver_path = "chromedriver.exe"
    service = Service(chromedriver_path)

    # Selenium browser setup
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Run Chrome in headless mode (without a GUI)
    browser = webdriver.Chrome(service=service, options=options)
    return browser


def parse_page(faq_links):
    faq_list = []
    for div in faq_links:
        link = div.find('a', attrs={'data-faqid': True})
        if link:
            question_text = link.text
            question_url = link.get('href')
            full_url = f'https://nu-kz.libanswers.com{question_url}'
            faq_list.append({
                'question': question_text,
                'url': full_url
            })
            print(f'Question: {question_text}')
            print(f'URL: {full_url}')
            print('---')
    return faq_list


def parse_answers_from_urls_sync(faq_list, browser):
    for question in faq_list:
        url = question.get('url')
        browser.get(url)
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        answer_div = soup.find('div', class_='s-la-faq-answer-body')
        if answer_div:
            answer_text = answer_div.text.strip()
            question['answer'] = answer_text
            print(f"Answer: {answer_text}\n")
        else:
            print("Answer not found.\n")
    return faq_list


if __name__ == '__main__':
    # Path to ChromeDriver

    browser = preprocess_browser()
    # URL of the page you want to scrape
    url = 'https://nu-kz.libanswers.com/search/'

    # Send a GET request to the page
    browser.get(url)
    browser.implicitly_wait(3)
    number_of_pages = 10
    faq_list = []
    for current_page in range(0, number_of_pages):
        try:
            # Find the pagination element. Adjust the selector as needed.
            next_page_button = browser.find_element(By.CSS_SELECTOR, f'a[data-page="{current_page + 1}"]')
            next_page_button.click()

            # Wait for the page to load. Adjust timing as needed.
            time.sleep(2)  # Example: wait for 5 seconds

            # Re-parse the page with BeautifulSoup
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            faq_links = soup.find_all('div', class_='s-srch-result-title')
            faq_list = faq_list + parse_page(faq_links)

        except Exception as e:
            print("Failed to click the next page button or scrape its content:", e)
            break
    answers = parse_answers_from_urls(faq_list, browser)
    browser.quit()
    print(answers)
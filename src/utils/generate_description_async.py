import openai
from openai import AsyncOpenAI
import re


def extract_book_names(text):
    pattern = r'"([^"]*)"'
    book_names = re.findall(pattern, text)
    return book_names


async def generate_description(input):
    messages = [{"role": "user",
                 "content":
                     """As a Book recommendation system, recommend several books, given that I liked this book: ' 
                     \n''"""},
                {"role": "user", "content": f"{input}"}]

    model = AsyncOpenAI()

    chat_completion = await model.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    reply = chat_completion.choices[0].message.content
    print(reply)
    book_names = extract_book_names(reply)
    print(book_names)
    return book_names

import openai
from openai import OpenAI


def generate_description(input):
    messages = [{"role": "user",
                 "content":
                     """As a Book recommendation system, recommend several books, given that I liked this book: ' 
                     \n''"""},
                {"role": "user", "content": f"{input}"}]

    model = OpenAI()

    chat_completion = model.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    reply = chat_completion.choices[0].message.content
    return reply

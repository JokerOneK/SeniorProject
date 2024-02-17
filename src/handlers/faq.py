import openai
from openai import AsyncOpenAI
from fastapi import APIRouter, HTTPException
from starlette import status

from src.dto.book_dto import Book
from src.dto.faq_dto import Question

router = APIRouter(
    prefix='/ask_question',
    tags=['ask_question'],

)


@router.post("/", status_code=status.HTTP_200_OK)
async def ask_question(question: Question):
    """
    This function provides response according to Frequently Asked Questions DataBase: \n
    :param book: question - string \n
    :return: answer - string
    """
    try:
        answer = await generate_response_to_the_question(f"{question.question}")
    except openai.APIConnectionError:
        raise HTTPException(status_code=403, detail='The server could not be reached')
    except openai.RateLimitError:
        raise HTTPException(status_code=403, detail='A 429 status code was received; we should back off a bit.')
    if answer is None:
        raise HTTPException(status_code=404, detail='Books not found')
    return {"Answer": answer}





async def generate_response_to_the_question(input):
    messages = [{"role": "user",
                 "content":
                     """
                     Imagine that you are Library System book assistant 
                     and I want to ask you a question. Your task is to generate common 
                     response to this question. My question: 
                     """},
                {"role": "user", "content": f"{input}"}]

    model = AsyncOpenAI()

    chat_completion = await model.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    reply = chat_completion.choices[0].message.content
    print(reply)
    return reply

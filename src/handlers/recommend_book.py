import openai
from fastapi import APIRouter, HTTPException
from starlette import status

from src.dto.book_dto import Book
from src.utils.generate_description_async import generate_description

router = APIRouter(
    prefix='/recommend',
    tags=['recommend'],

)


@router.post("/recommend_books", status_code=status.HTTP_200_OK)
async def recommend_books(book: Book):

    try:
        description = await generate_description(f"Book author name: {book.author}, title: {book.title}")
    except openai.APIConnectionError:
        raise HTTPException(status_code=403, detail='The server could not be reached')
    except openai.RateLimitError:
        raise HTTPException(status_code=403, detail='A 429 status code was received; we should back off a bit.')
    if description is None:
        raise HTTPException(status_code=404, detail='Books not found')
    return {"Recommended books": description}

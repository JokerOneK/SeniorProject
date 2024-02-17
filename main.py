from fastapi import FastAPI
import os

from src.dto.book_dto import Book
# from src.utils.generate_description import generate_description
from src.utils.generate_description_async import generate_description
from src.handlers import recommend_book, user, login, faq

os.environ["OPENAI_API_KEY"] = "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"

app = FastAPI()
app.include_router(recommend_book.router)
app.include_router(user.router)
app.include_router(login.router)
app.include_router(faq.router)
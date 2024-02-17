from pydantic import BaseModel, Field


class Book(BaseModel):
    author: str | None = Field(min_length=2, max_length=30, description="Provide the name of books author.")
    title: str | None = Field(min_length=2, description="Provide title of read book.")

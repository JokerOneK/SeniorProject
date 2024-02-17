from pydantic import BaseModel, Field


class Question(BaseModel):
    question: str | None = Field(min_length=2, max_length=256, description="Provide the question to AI Assistant.")

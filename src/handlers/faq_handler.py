import re
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.api import deps
from src.core.config import settings
from src.models.frequently_asked_questions import FrequentlyAskedQuestion
from src.utils.utils import validate_role


router = APIRouter(
    prefix='/faq',
    tags=['faq'],

)
def preprocess(text):
    stopwords = {"is", "can", "how", "what", "the", "a", "in", "of", "my"}
    words = re.findall(r'\w+', text.lower())
    return [word for word in words if word not in stopwords]


@router.post("/get_faq_answer/")
async def get_faq_answer(
        question,
        db: Session = Depends(deps.get_db),
):
    query = select(FrequentlyAskedQuestion)
    faqs = (db.scalars(query)).all()

    user_question_keywords = preprocess(question)

    max_matches = 0
    best_match_answer = "Sorry, I couldn't find an answer to your question."
    for faq in faqs:
        faq_keywords = preprocess(faq.question)
        common_keywords = set(user_question_keywords) & set(faq_keywords)
        if len(common_keywords) > max_matches:
            max_matches = len(common_keywords)
            best_match_answer = faq.url

    return {"answer": best_match_answer}
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.utils.faq_parser.faq_answer import faqs
from src.models.frequently_asked_questions import FrequentlyAskedQuestion

Base = declarative_base()

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/books"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


db = SessionLocal()
try:
    for faq in faqs:
        db_faq = FrequentlyAskedQuestion(question=faq["question"], url=faq["url"], answer=faq["answer"])
        db.add(db_faq)
    db.commit()
finally:
    db.close()
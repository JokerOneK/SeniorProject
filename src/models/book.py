from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Boolean, Column, Integer, VARCHAR, DateTime, FLOAT, INTEGER
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Book(Base):
    __tablename__ = "book"
    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(VARCHAR)
    description = Column(VARCHAR)
    authors = Column(VARCHAR)
    image = Column(VARCHAR)
    previewLink = Column(VARCHAR)
    publisher = Column(VARCHAR)
    publishedDate = Column(VARCHAR)
    infoLink = Column(VARCHAR)
    categories = Column(VARCHAR)
    ratingsCount = Column(FLOAT)

from sqlalchemy import Boolean, Column, text, VARCHAR, DateTime, FLOAT, INTEGER, BIGINT, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class RecommendedBooks(Base):
    __tablename__ = "recommended_books"
    id = Column(INTEGER, primary_key=True, index=True)
    book_id = Column(BIGINT, ForeignKey("book.id"))
    recommended_books = Column(ARRAY(VARCHAR), nullable=False, server_default=text('ARRAY[]::VARCHAR[]'))


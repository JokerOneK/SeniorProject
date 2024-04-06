from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Announcement(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    date = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.utcnow,
    )

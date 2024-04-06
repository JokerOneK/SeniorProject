from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class Announcement(BaseModel):
    id: int | None
    text: str
    #date: datetime | None


class AnnouncementOut(BaseModel):
    id: int | None
    text: str
    date: datetime | None
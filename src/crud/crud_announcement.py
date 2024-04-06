import datetime
from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.announcement import Announcement
from src.schemas.announcement import Announcement as AnnouncementDto


class CRUDAnnouncement(CRUDBase[Announcement, Announcement, Announcement]):

    def create(self, db: Session, *, obj_in: AnnouncementDto) -> Announcement:
        db_obj = Announcement(
            text=obj_in.text,
            date=datetime.datetime.utcnow()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Announcement, obj_in: Union[AnnouncementDto, Dict[str, Any]]
    ) -> Announcement:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


announcement = CRUDAnnouncement(Announcement)

from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.api import deps
from src.core.config import settings
from src.utils.utils import validate_role


router = APIRouter(
    prefix='/announcement',
    tags=['announcement'],

)


@router.get("/", response_model=List[schemas.AnnouncementOut])
def read_announcements(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve announcements.
    """
    announcements = crud.announcement.get_multi(db, skip=skip, limit=limit)
    return announcements


@router.post("/", response_model=schemas.AnnouncementOut)
def create_announcement(
    *,
    db: Session = Depends(deps.get_db),
    announcement_in: schemas.Announcement,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new announcement.
    """
    user = crud.announcement.create(db, obj_in=announcement_in)
    return user


@router.put("/announcement", response_model=schemas.AnnouncementOut)
def update_announcement(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    text: str,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update announcement.
    """
    current_announcement = crud.announcement.get(db, id)
    announcement_in = schemas.Announcement(id=id, text=text)
    announcement = crud.announcement.update(db, db_obj=current_announcement, obj_in=announcement_in)
    return announcement


@router.get("/{announcement_id}", response_model=schemas.AnnouncementOut)
def read_announcement_by_id(
    announcement_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    current_announcement = crud.announcement.get(db, announcement_id)
    return current_announcement


@router.delete("/{announcement_id}")
def remove_announcement_by_id(
    announcement_id: int,
    #current_user: models.User = Depends(deps.get_current_active_superuser),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    crud.announcement.remove(db, id=announcement_id)
    return 'Success'

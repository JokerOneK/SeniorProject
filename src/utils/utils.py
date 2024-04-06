import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import HTTPException
from jose import jwt
from starlette import status

from src.core.config import settings
from src.dto.user_dto import UserDto
from src.models import User


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return decoded_token["email"]
    except jwt.JWTError:
        return None


def validate_role(current_user: User, role: str):
    if role != current_user.role:
        raise HTTPException(
            detail="Недостаточно прав",
            status_code=status.HTTP_403_FORBIDDEN
        )

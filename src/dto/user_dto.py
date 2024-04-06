from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    full_name: str
    email: str
    is_active: bool
    is_super_user: bool
    role: str
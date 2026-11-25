from typing import Annotated
from uuid import uuid4

from pydantic import AfterValidator, BaseModel, EmailStr, Field


def validate_strong_password(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one number")

    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least on upper case character")

    return password


class BaseUser(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    name: str = Field(min_length=1, max_length=50)
    email: EmailStr


class UserCreate(BaseUser):
    password: Annotated[
        str,
        Field(min_length=8, max_length=50),
        AfterValidator(validate_strong_password),
    ]

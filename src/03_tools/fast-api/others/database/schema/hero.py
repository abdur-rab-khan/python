from datetime import UTC, datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import field_validator
from sqlmodel import DateTime, Field, Relationship, SQLModel


def utc_now():
    return datetime.now(UTC)


class Hero(SQLModel, table=True):
    __tablename__ = "heroes"

    secret_name: str
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    age: int | None = Field(default=None, ge=18, le=120)
    name: str = Field(index=True)  # 🟡 For making the current column as index
    user_id: UUID | None = Field(default=None, foreign_key="users.id")

    # 🟡 By Default it won't populate the joining data automatically and we don't need to manually use
    #    ".join()" method for joining the table
    # 🟡 By default when we try to fetch "Hero" SQLModel will automatically include the user
    user: Optional["User"] = Relationship(back_populates="heroes")

    # 🟡 Let's create fields that automatically filled like "createdAt" and "updatedAt"
    created_at: datetime = Field(
        default_factory=utc_now, sa_type=DateTime(timezone=True)
    )
    updated_at: datetime = Field(
        default_factory=utc_now,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"onupdate": utc_now},
    )

    # 🟡 Let's add custom validation for specifically to same
    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str):
        if not v.strip():
            raise ValueError("Name cannot be empty")

        if len(v.strip()) > 255:
            raise ValueError("Name must be within 255 characters")

        return v.strip()


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    age: int = Field(ge=18, le=120)
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    address: str | None = Field(default=None, max_length=255)

    # 🟡 Without """Relationship""" you join using ".join()" method that just gives you data as a pair
    #    than you manually join them by hand.
    # 🟡 Without """Relationship""" query User will automatically popular all the hero related to the
    #    user automatically.
    heroes: list[Hero] = Relationship(back_populates="user")

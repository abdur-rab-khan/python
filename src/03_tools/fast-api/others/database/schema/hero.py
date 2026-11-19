from uuid import uuid4

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    __tablename__ = "my_heroes"

    id: str = Field(default_factory=lambda: uuid4().hex, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str

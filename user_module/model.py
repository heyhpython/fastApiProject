from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(..., max_length=32)
    email: str = Field(..., max_length=64)
    hashed_password: str = Field(..., max_length=64)

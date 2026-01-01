from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

from app.shared.rules.user_rules import (
    MIN_USERNAME_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_EMAIL_LENGTH,
    MAX_EMAIL_LENGTH,
    MIN_FIRST_NAME_LENGTH,
    MAX_FIRST_NAME_LENGTH,
    MIN_LAST_NAME_LENGTH,
    MAX_LAST_NAME_LENGTH,

)


class GetUserOutputDTO(BaseModel):
    id: UUID
    email: EmailStr = Field(
        ...,
        min_length=MIN_EMAIL_LENGTH,
        max_length=MAX_EMAIL_LENGTH
    )
    username: str = Field(
        ...,
        min_length=MIN_USERNAME_LENGTH,
        max_length=MAX_USERNAME_LENGTH
    )
    first_name: str = Field(
        ...,
        min_length=MIN_FIRST_NAME_LENGTH,
        max_length=MAX_FIRST_NAME_LENGTH
    )
    last_name: str = Field(
        ...,
        min_length=MIN_LAST_NAME_LENGTH,
        max_length=MAX_LAST_NAME_LENGTH
    )
    roles: list[str]

from pydantic import BaseModel
from pydantic import field_validator
from pydantic import Field
from pydantic import EmailStr
from app.shared.utils.strings_predicate import (
    is_blank,
    contains_lowercase,
    contains_special,
    contains_uppercase,
    contains_digit,
)


class MeOutputDTO(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    roles: list[str]


class PatchMeInputDTO(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=254)
    username: str = Field(..., min_length=3, max_length=32)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)

    @field_validator("username")
    @classmethod
    def username_policy(cls, username: str) -> str:
        username = username.strip()

        if is_blank(username):
            raise ValueError("username must not be blank")

        if len(username) < 3:
            raise ValueError("username must be at least 3 characters long")

        if len(username) > 32:
            raise ValueError("username must be less than 32 characters")

        return username

    @field_validator("first_name")
    @classmethod
    def first_name_policy(cls, first_name: str) -> str:
        first_name = first_name.strip()

        if is_blank(first_name):
            raise ValueError("first name must not be blank")

        if len(first_name) < 1:
            raise ValueError("first name must be at least 1 character long")

        if len(first_name) > 100:
            raise ValueError("first name must be less than 100 characters")

        return first_name

    @field_validator("last_name")
    @classmethod
    def last_name_policu(cls, last_name: str) -> str:
        last_name.strip()

        if is_blank(last_name):
            raise ValueError("last name must not be blank")

        if len(last_name) < 1:
            raise ValueError("last name must be at least 1 character long")

        if len(last_name) > 100:
            raise ValueError("last name must be less than 100 characters")

        return last_name


class PasswordChangeDTO(BaseModel):
    current_password: str = Field(..., min_length=8, max_length=128)
    new_password: str = Field(..., min_length=8, max_length=128)

    @field_validator("new_password")
    @classmethod
    def password_policy(cls, password: str) -> str:
        password = password.strip()

        if is_blank(password):
            raise ValueError("password must not be blank")

        if len(password) < 8:
            raise ValueError("password must be at least 8 characters long")

        if len(password) > 128:
            raise ValueError("password must be less than 128 characters")

        if not contains_digit(password):
            raise ValueError("password must contain a digit")

        if not contains_lowercase(password):
            raise ValueError("password must contain a lowercase character")

        if not contains_uppercase(password):
            raise ValueError("password must contain an uppercase character")

        if not contains_special(password):
            raise ValueError("password must contain a special character")

        return password

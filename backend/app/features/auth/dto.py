from pydantic import BaseModel, UUID4, EmailStr, field_validator
import re

PASSWORD_REGEX = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).+$"
)

USERNAME_REGEX = re.compile(
    r"^[A-Za-z0-9_.-]+$"
)


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str

    @field_validator("password")
    @classmethod
    def password_policy(cls, v: str) -> str:
        v = v.strip()

        if len(v) < 8:
            raise ValueError("password must be at least 8 characters long")

        if not PASSWORD_REGEX.match(v):
            raise ValueError(
                "password must contain at least one uppercase letter, "
                "one lowercase letter, one digit, and one special character"
            )

        return v

    @field_validator("username")
    @classmethod
    def username_policy(cls, v: str) -> str:
        v = v.strip()

        if not USERNAME_REGEX.match(v):
            raise ValueError(
                "username may only contain letters, numbers, '_', '.', or '-'"
            )

        return v


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID4
    email: EmailStr

    class Config:
        from_attributes = True

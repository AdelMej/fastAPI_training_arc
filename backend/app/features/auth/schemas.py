from pydantic import BaseModel, UUID4, EmailStr, field_validator


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_policy(cls, v: str) -> str:
        if (len(v) < 8):
            raise ValueError("password must be at least 8 characters long")
        return v.strip()


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID4
    email: EmailStr

    class Config:
        from_attributes = True

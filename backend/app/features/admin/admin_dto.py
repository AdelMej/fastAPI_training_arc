from uuid import UUID
from pydantic import BaseModel, EmailStr


class GetUserOutputDTO(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    roles: list[str]

from typing import Protocol
from app.domain.user.user_entity import User


class UserRepository(Protocol):
    async def save(self, user: User) -> User: ...
    async def get_user_by_email(self, email: str) -> User | None: ...

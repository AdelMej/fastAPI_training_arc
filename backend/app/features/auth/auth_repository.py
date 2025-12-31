from typing import Protocol
from app.domain.user.user_entity import NewUserEntity, UserEntity


class AuthRepository(Protocol):
    async def create(self, user: NewUserEntity) -> UserEntity:
        ...

    async def exists_by_email(self, email: str) -> bool:
        ...

    async def exists_by_username(self, username: str) -> bool:
        ...

    async def find_user_by_email(self, email: str) -> UserEntity | None:
        ...

    async def find_user_by_username(self, username: str) -> UserEntity | None:
        ...

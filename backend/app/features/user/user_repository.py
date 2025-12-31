from typing import Protocol
from uuid import UUID
from app.domain.user.user_entity import UserEntity


class UserRepository(Protocol):
    async def update(self, user: UserEntity) -> None:
        ...

    async def exists_by_email(self, email: str) -> bool:
        ...

    async def exists_by_username(self, username: str) -> bool:
        ...

    async def find_user_by_email(self, email: str) -> UserEntity | None:
        ...

    async def find_user_by_username(self, username: str) -> UserEntity | None:
        ...

    async def find_user_by_id(self, user_id: UUID) -> UserEntity | None:
        ...

    async def delete_user_by_id(self, user_id: UUID) -> None:
        ...

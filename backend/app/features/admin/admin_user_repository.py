from typing import Protocol
from uuid import UUID
from app.domain.user.user_entity import UserEntity


class AdminUserRepository(Protocol):
    async def find_all_users(self) -> list[UserEntity]: ...
    async def find_user_by_id(self, user_id: UUID) -> UserEntity | None: ...

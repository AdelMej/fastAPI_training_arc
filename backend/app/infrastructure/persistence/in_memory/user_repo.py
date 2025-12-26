from uuid import uuid4
from uuid import UUID
from app.domain.user.user_entity import User


class InMemoryUserRepository:
    def __init__(self):
        self._users: dict[UUID, User] = {}

    async def save(self, user: User) -> User:
        if user.id is None:
            user.id = uuid4()
        self._users[user.id] = user
        return user

    async def exists_by_email(self, email: str) -> bool:
        return any(u.email == email for u in self._users.values())

    async def exists_by_username(self, username: str) -> bool:
        return any(u.username == username for u in self._users.values())

    async def find_user_by_email(self, email: str) -> User | None:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    async def find_user_by_username(self, username: str) -> User | None:
        for user in self._users.values():
            if user.username == username:
                return user
        return None

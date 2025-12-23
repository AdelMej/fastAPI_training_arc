from uuid import uuid4
from app.domain.user.user_entity import User


class InMemoryUserRepository:
    def __init__(self):
        self.users: dict[str, User] = {}

    async def save(self, user: User) -> User:
        if user.id is None:
            user.id = uuid4()
        self.users[user.email] = user
        return user

    async def get_user_by_email(self, email: str) -> User | None:
        return self.users.get(email)

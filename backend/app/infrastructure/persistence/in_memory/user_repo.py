from uuid import uuid4
from uuid import UUID
from app.domain.user.user_entity import NewUserEntity, UserEntity
from app.shared.security.password_hasher import PasswordHasher


class InMemoryUserRepository:
    def __init__(self, password_hasher: PasswordHasher):
        self._users: dict[UUID, UserEntity] = {}
        self._password_hasher = password_hasher

        admin = UserEntity(
            id=uuid4(),
            email="admin@example.com",
            username="admin",
            password_hash=password_hasher.hash("admin123"),
            first_name="admin",
            last_name="user",
            roles=["USER", "ADMIN"]
        )

        assert admin.id

        self._users[admin.id] = admin

    async def create(self, user: NewUserEntity) -> UserEntity:
        created = UserEntity(
            id=uuid4(),
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            password_hash=user.password_hash,
            roles=user.roles,
        )

        self._users[created.id] = created

        return created

    async def exists_by_email(self, email: str) -> bool:
        return any(u.email == email for u in self._users.values())

    async def exists_by_username(self, username: str) -> bool:
        return any(u.username == username for u in self._users.values())

    async def find_user_by_email(self, email: str) -> UserEntity | None:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    async def find_user_by_username(self, username: str) -> UserEntity | None:
        for user in self._users.values():
            if user.username == username:
                return user
        return None

    async def find_user_by_id(self, user_id: UUID) -> UserEntity | None:
        return self._users.get(user_id)

    async def find_all_users(self) -> list[UserEntity]:
        return list(self._users.values())

    async def delete_user_by_id(self, user_id: UUID) -> None:
        del self._users[user_id]

    async def update(self, user: UserEntity) -> None:
        self._users[user.id] = user

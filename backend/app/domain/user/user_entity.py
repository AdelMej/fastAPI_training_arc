from dataclasses import dataclass
from uuid import UUID


@dataclass
class UserEntity:
    id: UUID
    email: str
    username: str
    first_name: str
    last_name: str
    password_hash: str
    roles: list[str]

    async def update_user_profile(
        self,
        email: str,
        username: str,
        first_name: str,
        last_name: str
    ) -> None:
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name


@dataclass
class NewUserEntity:
    email: str
    username: str
    first_name: str
    last_name: str
    password_hash: str
    roles: list[str]

    async def update_user_profile(
        self,
        email: str,
        username: str,
        first_name: str,
        last_name: str
    ) -> None:
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

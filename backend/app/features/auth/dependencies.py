from functools import lru_cache

from fastapi import Depends
from app.infrastructure.persistence import InMemoryUserRepository
from app.features.auth.service import AuthService
from app.features.auth.repository import UserRepository
from app.infrastructure.password.argon2_hasher import get_password_hasher
from app.shared.security.password_hasher import PasswordHasher

_repo = InMemoryUserRepository()


@lru_cache
def get_user_repo() -> UserRepository:
    return _repo


def get_auth_service(
    repo: UserRepository = Depends(get_user_repo),
    password_hasher: PasswordHasher = Depends(get_password_hasher)
) -> AuthService:

    return AuthService(
        repo=repo,
        password_hasher=password_hasher,
    )

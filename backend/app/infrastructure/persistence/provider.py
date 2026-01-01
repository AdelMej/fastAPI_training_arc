from functools import lru_cache

from fastapi import Depends
from app.features.admin.book.admin_book_repository import AdminBookRepository
from app.features.admin.user.admin_user_repository import AdminUserRepository
from app.features.auth.auth_repository import AuthRepository
from app.features.book.book_repository import BookRepository
from app.features.user.user_repository import UserRepository
from app.infrastructure.persistence import InMemoryUserRepository
from app.infrastructure.password.provider import get_password_hasher
from app.infrastructure.persistence import InMemoryBookRepository
from app.shared.security.password_hasher import PasswordHasher


@lru_cache
def get_user_repository(
    password_hasher: PasswordHasher = Depends(get_password_hasher)
) -> InMemoryUserRepository:
    return InMemoryUserRepository(password_hasher=password_hasher)


def get_user_repo(
    repo: InMemoryUserRepository = Depends(get_user_repository)
) -> UserRepository:
    return repo


def get_auth_repo(
    repo: InMemoryUserRepository = Depends(get_user_repository)
) -> AuthRepository:
    return repo


def get_admin_user_repo(
        repo: InMemoryUserRepository = Depends(get_user_repository)
) -> AdminUserRepository:
    return repo


@lru_cache
def get_book_repository(
) -> BookRepository:
    return InMemoryBookRepository()


def get_admin_book_repo(
        repo: InMemoryBookRepository = Depends(get_book_repository)
) -> AdminBookRepository:
    return repo

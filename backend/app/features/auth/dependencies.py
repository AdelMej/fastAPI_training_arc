from app.infrastructure.persistence import InMemoryUserRepository
from app.features.auth.service import AuthService
from app.shared.security.password_hasher import PasswordHasher
from app.features.auth.repository import UserRepository

_repo = InMemoryUserRepository()


def get_user_repo() -> UserRepository:
    return _repo


def get_password_hasher() -> PasswordHasher:
    return PasswordHasher()


def get_auth_service() -> AuthService:
    return AuthService(
        repo=get_user_repo(),
        password_hasher=get_password_hasher()
    )

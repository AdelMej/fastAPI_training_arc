from fastapi import Depends

# service
from app.features.auth.auth_service import AuthService

# persistence
from app.features.auth.auth_repository import AuthRepository
from app.infrastructure.persistence.provider import get_auth_repo

# password hasher
from app.infrastructure.password.provider import get_password_hasher
from app.shared.security.password_hasher import PasswordHasher


def get_auth_service(
    repo: AuthRepository = Depends(get_auth_repo),
    password_hasher: PasswordHasher = Depends(get_password_hasher)
) -> AuthService:

    return AuthService(
        repo=repo,
        password_hasher=password_hasher,
    )

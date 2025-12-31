from fastapi import Depends
from app.features.user.user_service import UserService
from app.infrastructure.persistence.provider import get_user_repo
from app.features.user.user_repository import UserRepository
from app.infrastructure.password.provider import get_password_hasher
from app.shared.security.password_hasher import PasswordHasher


def get_user_service(
    repo: UserRepository = Depends(get_user_repo),
    password_hasher: PasswordHasher = Depends(get_password_hasher)
):
    return UserService(repo=repo, password_hasher=password_hasher)

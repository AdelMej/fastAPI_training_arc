from fastapi import Depends
from app.features.admin.user.admin_user_service import AdminUserService
from app.features.admin.user.admin_user_repository import AdminUserRepository
from app.infrastructure.persistence.provider import get_user_repo


def get_admin_user_repo(
        repo: AdminUserService = Depends(get_user_repo)
) -> AdminUserService:
    return repo


def get_admin_user_service(
    repo: AdminUserRepository = Depends(get_admin_user_repo)
) -> AdminUserService:
    return AdminUserService(repo)

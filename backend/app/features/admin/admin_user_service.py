from uuid import UUID
from app.domain.user.user_authorization_rules import ensure_user_is_admin
from app.domain.user.user_entity import UserEntity
from app.features.admin.admin_user_repository import AdminUserRepository
from app.shared.exceptions.commons import ForbiddenError, NotFoundError


class AdminUserService:
    def __init__(
            self,
            repo: AdminUserRepository
    ) -> None:
        self._repo = repo

    async def get_all_users(self, actor: UserEntity) -> list[UserEntity]:
        if actor.id is None:
            raise RuntimeError("")
        user = await self._repo.find_user_by_id(actor.id)
        if not user:
            raise ForbiddenError()

        ensure_user_is_admin(user)
        return await self._repo.find_all_users()

    async def get_user_by_id(
            self,
            actor: UserEntity,
            target: UUID
    ) -> UserEntity:
        ensure_user_is_admin(actor)

        result = await self._repo.find_user_by_id(target)
        if not result:
            raise NotFoundError()

        return result

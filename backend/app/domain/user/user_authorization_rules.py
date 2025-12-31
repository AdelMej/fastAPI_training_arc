from app.domain.user.user_entity import UserEntity
from app.domain.user.user_exceptions import UserAccessDeniedError

ADMIN_ROLE = "ADMIN"


def ensure_user_is_admin(actor: UserEntity) -> None:
    if ADMIN_ROLE not in actor.roles:
        raise UserAccessDeniedError()


def ensure_user_can_access_user(actor: UserEntity, target: UserEntity) -> None:
    if ADMIN_ROLE in actor.roles:
        return

    if actor.id != target.id:
        raise UserAccessDeniedError()

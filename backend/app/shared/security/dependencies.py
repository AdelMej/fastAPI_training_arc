from fastapi import Security, Depends
from app.features.user.user_repository import UserRepository
from app.infrastructure.persistence.provider import get_user_repo
from app.shared.security.jwt import JWTService, TokenSubject
from app.infrastructure.jwt.provider import get_jwt_service
from fastapi.security import OAuth2PasswordBearer
from app.domain.user.user_entity import UserEntity
from app.shared.exceptions.commons import (
        ForbiddenError,
        UnauthorizedError
)
from app.shared.rules.role_rules import ROLE_ADMIN

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_current_subject(
    token: str = Security(_oauth2_scheme),
    jwt_service: JWTService = Depends(get_jwt_service)
) -> TokenSubject:
    return jwt_service.decode_access_token(token)


async def get_current_user(
    subject: TokenSubject = Depends(get_current_subject),
    repo: UserRepository = Depends(get_user_repo)
) -> UserEntity:

    user = await repo.find_user_by_id(subject.user_id)

    if not user:
        raise UnauthorizedError()

    return user


async def get_admin(
    actor: UserEntity = Depends(get_current_user)
) -> UserEntity:

    if ROLE_ADMIN not in actor.roles:
        raise ForbiddenError()

    return actor

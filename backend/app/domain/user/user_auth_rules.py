from app.domain.user.user_entity import UserEntity
from app.domain.user.user_exceptions import (
        InvalidIdentifierError,
        InvalidPasswordError
)
from app.shared.security.password_hasher import PasswordHasher


def ensure_user_can_authenticate(
    user: UserEntity | None,
    plain_password: str,
    password_hasher: PasswordHasher,
) -> UserEntity:

    if not user:
        raise InvalidIdentifierError()

    if not password_hasher.verify(plain_password, user.password_hash):
        raise InvalidPasswordError()

    return user

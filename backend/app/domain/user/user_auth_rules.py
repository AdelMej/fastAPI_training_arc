from app.domain.user.user_entity import User
from app.domain.user.exceptions import InvalidCredentialsError
from app.shared.security.password_hasher import PasswordHasher


def ensure_user_can_authenticate(
    user: User | None,
    plain_password: str,
    password_hasher: PasswordHasher,
) -> None:

    if not user:
        raise InvalidCredentialsError()

    if not password_hasher.verify(plain_password, user.password_hash):
        raise InvalidCredentialsError()

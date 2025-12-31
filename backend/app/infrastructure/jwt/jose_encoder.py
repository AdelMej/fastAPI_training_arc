from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
from uuid import UUID

from app.infrastructure.config.jwt import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.shared.security.jwt import JWTService, TokenSubject
from app.infrastructure.jwt.exceptions import InvalidTokenError


class JoseJWTService(JWTService):
    def __init__(self):
        self._secret_key = SECRET_KEY
        self._algorithm = ALGORITHM
        self._expire_minutes = ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, *, subject: TokenSubject) -> str:
        now = datetime.now(tz=timezone.utc)

        payload = {
            "sub": str(subject.user_id),
            "roles": subject.roles,
            "iat": int(now.timestamp()),
            "exp": int(
                (now + timedelta(minutes=self._expire_minutes)).timestamp()
            ),
        }

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def decode_access_token(self, token: str) -> TokenSubject:
        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=ALGORITHM
            )
        except JWTError:
            raise InvalidTokenError()

        subject = payload.get("sub")
        if not subject:
            raise InvalidTokenError()

        return TokenSubject(
            user_id=(UUID(payload["sub"])),
            roles=(payload["roles"]),
        )

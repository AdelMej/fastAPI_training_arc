from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.infrastructure.config.jwt import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


class InvalidTokenError(Exception):
    pass


def create_access_token(subject: str) -> str:
    expire = datetime.now() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def validate_access_token(token: str) -> str:
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

    return subject

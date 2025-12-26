from app.domain.user.exceptions import PasswordTooWeakError
from app.domain.user.exceptions import UsernameTooShortError
from app.domain.user.exceptions import InvalidEmailError
from zxcvbn import zxcvbn
import re

MIN_PASSWORD_LENGTH = 8
MIN_ZXCVBN_SCORE = 3
MIN_USERNAME_LENGTH = 3
MAX_EMAIL_LENGTH = 254
MAX_LOCAL_PART = 64
EMAIL_REGEX = re.compile(
    r"^[a-z0-9._%+-]+@[a-z0-9-]+(\.[a-z0-9-]+)+$"
)


def ensure_password_is_strong(password: str):
    if len(password) < MIN_PASSWORD_LENGTH:
        raise PasswordTooWeakError(
            "password must be at least 8 character long"
        )

    result = zxcvbn(password)

    if result["score"] < MIN_ZXCVBN_SCORE:
        raise PasswordTooWeakError(
            "password does not meet strength requirements"
        )


def ensure_username_is_valid(username: str):
    if len(username) < MIN_USERNAME_LENGTH:
        raise UsernameTooShortError


def ensure_email_is_valid(email: str):
    if len(email) > MAX_EMAIL_LENGTH:
        raise InvalidEmailError("email is too long")

    local, _, domain = email.partition("@")

    if not local or not domain:
        raise InvalidEmailError("email is invalid")

    if len(local) > MAX_LOCAL_PART:
        raise InvalidEmailError("email local part is too long")

    if not EMAIL_REGEX.match(email):
        raise InvalidEmailError("email is invalid")

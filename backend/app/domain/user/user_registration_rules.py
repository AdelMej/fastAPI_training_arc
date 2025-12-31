from app.domain.user.user_exceptions import (
    EmailIsBlankError,
    EmailIsTooLong,
    EmailIsTooShort,
    EmailLocalPartTooLong,
    EmailMissingAtSymbolError,
    EmailMissingDomainError,
    EmailMissingLocalError,
    FirstNameIsBlankError,
    FirstNameTooLongError,
    FirstNameTooShortError,
    LastNameIsBlankError,
    LastNameTooLongError,
    LastNameTooShortError,
    PasswordIsBlankError,
    PasswordMissingDigitError,
    PasswordMissingLowercaseError,
    PasswordMissingSpecialCharError,
    PasswordMissingUppercaseError,
    PasswordTooLongError,
    PasswordTooShortError,
    PasswordTooWeakError,
    UsernameIsBlankError,
    UsernameTooShortError,
    UsernameTooLongError,
)

from app.shared.utils.strings_predicate import (
    is_blank,
    contains_lowercase,
    contains_digit,
    contains_uppercase,
    contains_special,
)


from zxcvbn import zxcvbn

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128
MIN_ZXCVBN_SCORE = 3

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 32

MIN_EMAIL_LENGTH = 3
MAX_EMAIL_LENGTH = 254
MAX_LOCAL_PART = 64

MIN_FIRST_NAME_LENGTH = 1
MAX_FIRST_NAME_LENGTH = 100

MIN_LAST_NAME_LENGTH = 1
MAX_LAST_NAME_LENGTH = 100


def ensure_password_is_strong(password: str):
    if is_blank(password):
        raise PasswordIsBlankError()

    if len(password) < MIN_PASSWORD_LENGTH:
        raise PasswordTooShortError()

    if len(password) > MAX_PASSWORD_LENGTH:
        raise PasswordTooLongError()

    if not contains_lowercase(password):
        raise PasswordMissingLowercaseError()

    if not contains_uppercase(password):
        raise PasswordMissingUppercaseError()

    if not contains_digit(password):
        raise PasswordMissingDigitError()

    if not contains_special(password):
        raise PasswordMissingSpecialCharError()

    result = zxcvbn(password)

    if result["score"] < MIN_ZXCVBN_SCORE:
        raise PasswordTooWeakError()


def ensure_username_is_valid(username: str):
    if is_blank(username):
        raise UsernameIsBlankError()

    if len(username) < MIN_USERNAME_LENGTH:
        raise UsernameTooShortError()

    if len(username) > MAX_USERNAME_LENGTH:
        raise UsernameTooLongError()


def ensure_email_is_valid(email: str):
    if is_blank(email):
        raise EmailIsBlankError()

    if len(email) < MIN_EMAIL_LENGTH:
        raise EmailIsTooShort()

    if len(email) > MAX_EMAIL_LENGTH:
        raise EmailIsTooLong()

    if "@" not in email:
        raise EmailMissingAtSymbolError()

    local, _, domain = email.partition("@")

    if not local:
        raise EmailMissingLocalError()

    if not domain:
        raise EmailMissingDomainError()

    if len(local) > MAX_LOCAL_PART:
        raise EmailLocalPartTooLong()


def ensure_first_name_is_valid(first_name: str):
    if is_blank(first_name):
        raise FirstNameIsBlankError()

    if len(first_name) < MIN_FIRST_NAME_LENGTH:
        raise FirstNameTooShortError()

    if len(first_name) > MAX_FIRST_NAME_LENGTH:
        raise FirstNameTooLongError()


def ensure_last_name_is_valid(last_name: str):
    if is_blank(last_name):
        raise LastNameIsBlankError()

    if len(last_name) < MIN_LAST_NAME_LENGTH:
        raise LastNameTooShortError()

    if len(last_name) > MAX_LAST_NAME_LENGTH:
        raise LastNameTooLongError()

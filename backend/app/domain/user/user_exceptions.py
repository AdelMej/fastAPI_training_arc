from app.shared.security import password_hasher


class UserDomainError(Exception):
    """Base user domain error"""
    pass


# --- Registartion exception ---
class EmailConflictError(UserDomainError):
    pass


class UsernameConflictError(UserDomainError):
    pass


# --- Username exceptions ---
class UsernameAlreadyExistError(UserDomainError):
    pass


class UsernameIsBlankError(UserDomainError):
    pass


class UsernameTooShortError(UserDomainError):
    pass


class UsernameTooLongError(UserDomainError):
    pass


# --- Password exceptions ---
class PasswordTooWeakError(UserDomainError):
    pass


class PasswordTooShortError(UserDomainError):
    pass


class PasswordTooLongError(UserDomainError):
    pass


class PasswordMissingLowercaseError(UserDomainError):
    pass


class PasswordMissingUppercaseError(UserDomainError):
    pass


class PasswordMissingDigitError(UserDomainError):
    pass


class PasswordMissingSpecialCharError(UserDomainError):
    pass


class PasswordIsBlankError(UserDomainError):
    pass


class InvalidCurrentPasswordError(UserDomainError):
    pass


class NewPasswordSameAsOldError(UserDomainError):
    pass


# --- First name exceptions ---
class FirstNameTooShortError(UserDomainError):
    pass


class FirstNameTooLongError(UserDomainError):
    pass


class FirstNameIsBlankError(UserDomainError):
    pass


# --- Last name exceptions ---
class LastNameIsBlankError(UserDomainError):
    pass


class LastNameTooShortError(UserDomainError):
    pass


class LastNameTooLongError(UserDomainError):
    pass


# --- Email exceptions ---
class EmailAlreadyExistError(UserDomainError):
    pass


class EmailIsBlankError(UserDomainError):
    pass


class EmailIsTooShort(UserDomainError):
    pass


class EmailIsTooLong(UserDomainError):
    pass


class EmailLocalPartTooLong(UserDomainError):
    pass


class EmailMissingAtSymbolError(UserDomainError):
    pass


class EmailMissingLocalError(UserDomainError):
    pass


class EmailMissingDomainError(UserDomainError):
    pass


# --- Auth exceptions ---
class UserAccessDeniedError(UserDomainError):
    pass


class InvalidIdentifierError(UserDomainError):
    pass


class InvalidPasswordError(UserDomainError):
    pass


# --- Update exceptions ---
class NoFieldToUpdateError(UserDomainError):
    pass

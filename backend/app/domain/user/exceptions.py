class UserDomainError(Exception):
    """Base user domain error"""


class InvalidCredentialsError(UserDomainError):
    pass


class UserAlreadyExistsError(UserDomainError):
    pass

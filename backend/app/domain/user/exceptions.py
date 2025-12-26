class UserDomainError(Exception):
    """Base user domain error"""
    code: str = "business_rule_violation"
    fields: dict[str, str] | None = None

    def __init__(
        self,
        message: str | None = None,
        *,
        fields: dict[str, str] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.fields = fields


class InvalidCredentialsError(UserDomainError):
    code = "invalid_credentials"


class UserAlreadyExistsError(UserDomainError):
    code = "user_already_exists"


class UsernameTooShortError(UserDomainError):
    code = "validation_error"

    def __init__(self):
        super().__init__(
            fields={"username": "username too short"}
        )


class PasswordTooWeakError(UserDomainError):
    code = "validation_error"

    def __init__(self, reason: str):
        super().__init__(
                fields={"password": reason}
        )


class InvalidEmailError(UserDomainError):
    code = "validation_error"

    def __init__(self, reason: str):
        super().__init__(
            fields={"email": reason}
        )

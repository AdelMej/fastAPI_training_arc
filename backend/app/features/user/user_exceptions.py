class UserApplicationError(Exception):
    """
    Base class for application-level errors
    that are meant to be translated to HTTP responses.
    """
    status_code: int = 500
    error_code: str = "auth_application_error"

    def __init__(self):
        super().__init__(self.error_code)


class UpdateFailureError(UserApplicationError):
    status_code: int = 400
    error_code: str = "update_failure_error"


class InvalidPasswordError(UserApplicationError):
    status_code: int = 400
    error_code: str = "invalid_password_change"

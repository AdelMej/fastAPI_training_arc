class AuthApplicationError(Exception):
    """
    Base class for application-level errors
    that are meant to be translated to HTTP responses.
    """
    status_code: int = 500
    error_code: str = "auth_application_error"

    def __init__(self):
        super().__init__(self.error_code)


class InvalidCredentialsError(AuthApplicationError):
    status_code = 401
    error_code = "invalid_credentials"


class RegistrationFailureError(AuthApplicationError):
    status_code = 400
    error_code = "registration_failed"

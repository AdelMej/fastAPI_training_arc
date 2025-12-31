class CommonError(Exception):
    status_code: int = 500
    error_code: str = "internal_error"

    def __init__(self):
        super().__init__(self.error_code)


class UnauthorizedError(CommonError):
    status_code = 401
    error_code = "unauthorized"


class ForbiddenError(CommonError):
    status_code = 403
    error_code = "forbidden"


class NotFoundError(CommonError):
    status_code = 404
    error_code = "not_found"

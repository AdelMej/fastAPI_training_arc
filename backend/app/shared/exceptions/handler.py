from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def validation_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    assert isinstance(exc, RequestValidationError)

    return JSONResponse(
        status_code=422,
        content={
            "error": "validation_error",
            "fields": exc.errors(),
        },
    )

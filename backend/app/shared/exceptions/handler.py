from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.domain.user.exceptions import UserDomainError

from typing import cast, Any


# -------- Validation errors (DTOs) --------
def validation_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    validation_exc = cast(RequestValidationError, exc)

    fields = {}

    # extracting error messages from exception
    for error in validation_exc.errors():
        field = error["loc"][-1]

        fields[field] = clean_validation_message(error["msg"])

    return JSONResponse(
        status_code=422,
        content={
            "error": "validation_error",
            "fields": fields,
        },
    )


def clean_validation_message(message: str) -> str:
    prefixes = (
        "Value error, ",
        "value error, ",
    )

    for prefix in prefixes:
        if message.startswith(prefix):
            return message[len(prefix):]

    return message


# -------- Domain errors --------
def user_domain_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    domain_exc = cast(UserDomainError, exc)

    content: dict[str, Any] = {
        "error": domain_exc.code,
    }

    if domain_exc.fields:
        content["fields"] = domain_exc.fields

    return JSONResponse(
        status_code=400,
        content=content
    )

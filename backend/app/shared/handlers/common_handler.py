from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from typing import cast

from app.shared.exceptions.commons import (
    UnauthorizedError,
    ForbiddenError,
    NotFoundError
)


def register_handlers(app: FastAPI) -> None:

    # -----------------------
    # --- common handlers ---
    # -----------------------

    @app.exception_handler(UnauthorizedError)
    async def unauthorized_handler(
            request: Request,
            exc: UnauthorizedError
    ):
        return JSONResponse(
            status_code=401,
            content={"error": "unauthorized"}
        )

    @app.exception_handler(ForbiddenError)
    async def forbidden_handler(
            request: Request,
            exc: ForbiddenError
    ):
        return JSONResponse(
            status_code=401,
            content={"error": "forbidden"}
        )

    @app.exception_handler(NotFoundError)
    async def not_found_handler(
            request: Request,
            exc: ForbiddenError
    ):
        return JSONResponse(
            status_code=404,
            content={"error": "not_found"}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
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

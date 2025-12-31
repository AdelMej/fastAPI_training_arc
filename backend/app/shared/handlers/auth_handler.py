from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.features.auth.auth_exceptions import (
        RegistrationFailureError,
        InvalidCredentialsError
)


def register_handlers(app: FastAPI) -> None:

    # ----------------------------
    # --- Registration handler ---
    # ----------------------------

    @app.exception_handler(RegistrationFailureError)
    async def registration_error_handler(
            request: Request,
            exc: RegistrationFailureError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "registration_failure"}
        )

    # ---------------------
    # --- Login handler ---
    # ---------------------

    @app.exception_handler(InvalidCredentialsError)
    async def invalid_credentials_handler(
        request: Request,
        exc: InvalidCredentialsError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=401,
            content={"error": "invalid credentials"}
        )

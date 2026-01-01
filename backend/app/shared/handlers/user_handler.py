from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request

from app.domain.user.user_exceptions import (
    PasswordIsBlankError,
    PasswordTooWeakError,
    PasswordTooShortError,
    PasswordTooLongError,
    PasswordMissingLowercaseError,
    PasswordMissingUppercaseError,
    PasswordMissingDigitError,
    PasswordMissingSpecialCharError,
    EmailIsBlankError,
    EmailIsTooShort,
    EmailIsTooLong,
    EmailMissingAtSymbolError,
    EmailMissingLocalError,
    EmailMissingDomainError,
    EmailLocalPartTooLong,
    UsernameIsBlankError,
    UsernameTooShortError,
    UsernameTooLongError,
    FirstNameIsBlankError,
    FirstNameTooShortError,
    FirstNameTooLongError,
    LastNameIsBlankError,
    LastNameTooShortError,
    LastNameTooLongError,
    NoFieldToUpdateError
)


from app.features.user.user_exceptions import (
    UpdateFailureError,
    InvalidPasswordError
)

from app.shared.rules.password_rules import (
    MIN_PASSWORD_LENGTH,
    MAX_PASSWORD_LENGTH
)

from app.shared.rules.user_rules import (
    MIN_EMAIL_LENGTH,
    MAX_EMAIL_LENGTH,
    MAX_LOCAL_PART,
    MIN_USERNAME_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_FIRST_NAME_LENGTH,
    MAX_FIRST_NAME_LENGTH,
    MIN_LAST_NAME_LENGTH,
    MAX_LAST_NAME_LENGTH
)


def register_handlers(app: FastAPI) -> None:

    # -------------------------
    # --- Password handlers ---
    # -------------------------

    @app.exception_handler(PasswordIsBlankError)
    async def password_is_blank_handler(
            request: Request,
            exc: PasswordIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "password must not be blank"}
        )

    @app.exception_handler(PasswordTooWeakError)
    async def password_is_weak_handler(
            request: Request,
            exc: PasswordTooWeakError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "password doesn't meet strength requirements"}
        )

    @app.exception_handler(PasswordTooShortError)
    async def password_too_short_handler(
            request: Request,
            exc: PasswordTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "password must be at least {} character long"
                .format(MIN_PASSWORD_LENGTH)
            }
        )

    @app.exception_handler(PasswordTooLongError)
    async def password_too_long_handler(
            request: Request,
            exc: PasswordTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "password must be less than {} character"
                .format(MAX_PASSWORD_LENGTH)
            }
        )

    @app.exception_handler(PasswordMissingLowercaseError)
    async def password_missing_lowercase_handler(
            request: Request,
            exc: PasswordMissingLowercaseError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "password must contain a lowercase character"}
        )

    @app.exception_handler(PasswordMissingUppercaseError)
    async def password_missing_uppercase_handler(
            request: Request,
            exc: PasswordMissingUppercaseError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "password must contain an uppercase character"}
        )

    @app.exception_handler(PasswordMissingDigitError)
    async def password_missing_digit_handler(
            request: Request,
            exc: PasswordMissingDigitError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "password must contain a digit"}
        )

    @app.exception_handler(PasswordMissingSpecialCharError)
    async def password_missing_special_char_handler(
            request: Request,
            exc: PasswordMissingSpecialCharError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "password must contain a special character"}
        )

    @app.exception_handler(InvalidPasswordError)
    async def invalid_password_handler(
        request: Request,
        exc: InvalidPasswordError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "invalid password"}
        )
    # ----------------------
    # --- Email handlers ---
    # ----------------------

    @app.exception_handler(EmailIsBlankError)
    async def email_is_blank_handler(
            request: Request,
            exc: EmailIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "email must not be blank"}
        )

    @app.exception_handler(EmailIsTooShort)
    async def email_too_short_handler(
            request: Request,
            exc: EmailIsTooShort
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "email must be at least {} characters long"
                .format(MIN_EMAIL_LENGTH)
            }
        )

    @app.exception_handler(EmailIsTooLong)
    async def email_too_long_handler(
            request: Request,
            exc: EmailIsTooLong
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "email must be less than {} characters long"
                .format(MAX_EMAIL_LENGTH)
            }
        )

    @app.exception_handler(EmailMissingAtSymbolError)
    async def email_missin_at_symbol_handler(
            request: Request,
            exc: EmailMissingAtSymbolError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "email must contain the at symbol"}
        )

    @app.exception_handler(EmailMissingLocalError)
    async def email_missing_local_handler(
            request: Request,
            exc: EmailMissingLocalError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "email must contain a local-part"}
        )

    @app.exception_handler(EmailMissingDomainError)
    async def email_missing_domain_handler(
            request: Request,
            exc: EmailMissingDomainError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "email must contain a domain"}
        )

    @app.exception_handler(EmailLocalPartTooLong)
    async def email_local_part_too_long_handler(
            request: Request,
            exc: EmailLocalPartTooLong
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "email local-part must be less than {} characters"
                .format(MAX_LOCAL_PART)
            }
        )

    # -------------------------
    # --- Username handlers ---
    # -------------------------

    @app.exception_handler(UsernameIsBlankError)
    async def username_is_blank_handler(
            request: Request,
            exc: UsernameIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "username must not be blank"}
        )

    @app.exception_handler(UsernameTooShortError)
    async def username_too_short_handler(
            request: Request,
            exc: UsernameTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "username must be at least {} characters long"
                .format(MIN_USERNAME_LENGTH)
            }
        )

    @app.exception_handler(UsernameTooLongError)
    async def username_too_long_handler(
            request: Request,
            exc: UsernameTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "username must be less than {} characters"
                .format(MAX_USERNAME_LENGTH)
            }
        )

    # ---------------------------
    # --- First name handlers ---
    # ---------------------------

    @app.exception_handler(FirstNameIsBlankError)
    async def firstname_is_blank_handler(
            request: Request,
            exc: FirstNameIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "first name must not be blank"}
        )

    @app.exception_handler(FirstNameTooShortError)
    async def firstname_too_short_handler(
            request: Request,
            exc: FirstNameTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "first name must be at least {} character long"
                .format(MIN_FIRST_NAME_LENGTH)
            }
        )

    @app.exception_handler(FirstNameTooLongError)
    async def firstname_too_long_handler(
            request: Request,
            exc: FirstNameTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "first name must be less than {} characters"
                .format(MAX_FIRST_NAME_LENGTH)
            }
        )

    # --------------------------
    # --- Last name handlers ---
    # --------------------------

    @app.exception_handler(LastNameIsBlankError)
    async def lastname_is_blank_handler(
            request: Request,
            exc: LastNameIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "last name must not be blank"}
        )

    @app.exception_handler(LastNameTooShortError)
    async def last_name_too_short_handler(
            request: Request,
            exc: LastNameTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "last name must be at least {} character long"
                .format(MIN_LAST_NAME_LENGTH)
            }
        )

    @app.exception_handler(LastNameTooLongError)
    async def last_name_too_long_handler(
            request: Request,
            exc: LastNameTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "last name must be at least {} characters long"
                .format(MAX_LAST_NAME_LENGTH)
            }
        )

    # -----------------------
    # --- Update handlers ---
    # -----------------------

    @app.exception_handler(NoFieldToUpdateError)
    async def no_field_to_update_handler(
            request: Request,
            exc: NoFieldToUpdateError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "no fields to update"}
        )

    @app.exception_handler(UpdateFailureError)
    async def update_failure_error(
            request: Request,
            exc: UpdateFailureError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "update failed"}
        )

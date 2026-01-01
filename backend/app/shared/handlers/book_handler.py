from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from app.domain.book.book_exceptions import (
    IsbnAlreadyExist,
    IsbnIsBlankError,
    InvalidIsbnError,
    TitleIsBlankError,
    TitleTooShortError,
    TitleTooLongError,
    AuthorIsBlankError,
    AuthorTooShortError,
    AuthorTooLongError,
    PagesTooLowError,
    PagesTooHighError,
    LanguageIsBlankError,
    LanguageTooLongError,
    LanguageTooShortError,
    YearTooLowError,
    YearTooHighError,
    DescriptionTooLongError,
)

from app.shared.rules.book_rules import (
    MIN_TITLE_LENGTH,
    MAX_TITLE_LENGTH,
    MIN_AUTHOR_LENGTH,
    MAX_AUTHOR_LENGTH,
    MIN_PAGES,
    MAX_PAGES,
    MIN_LANGUAGE_LENGTH,
    MAX_LANGUAGE_LENGTH,
    MIN_YEAR,
    CURRENT_YEAR,
    MAX_BOOK_DESCRIPTION_LENGTH
)


def register_handlers(app: FastAPI) -> None:

    # ---------------------
    # --- Isbn Handlers ---
    # ---------------------

    @app.exception_handler(IsbnAlreadyExist)
    async def isbn_already_exist_handler(
            request: Request,
            exc: IsbnAlreadyExist
    ) -> JSONResponse:
        return JSONResponse(
            status_code=409,
            content={"error": "isbn already exist"}
        )

    @app.exception_handler(IsbnIsBlankError)
    async def isbn_is_blank_handler(
            request: Request,
            exc: IsbnIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "isbn must not be blank"}
        )

    @app.exception_handler(InvalidIsbnError)
    async def invalid_isbn_handler(
            request: Request,
            exc: InvalidIsbnError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "isbn must be valid"}
        )

    # ----------------------
    # --- Title handlers ---
    # ----------------------

    @app.exception_handler(TitleIsBlankError)
    async def title_is_blank_handler(
            request: Request,
            exc: TitleIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "title must not be blank"}
        )

    @app.exception_handler(TitleTooShortError)
    async def title_too_short_handler(
            request: Request,
            exc: TitleTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "title must be at least {} characters long"
                .format(MIN_TITLE_LENGTH)
            }
        )

    @app.exception_handler(TitleTooLongError)
    async def title_too_long_handler(
            request: Request,
            exc: TitleTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "title must be less than {} character"
                .format(MAX_TITLE_LENGTH)
            }
        )

    # -----------------------
    # --- Author handlers ---
    # -----------------------

    @app.exception_handler(AuthorIsBlankError)
    async def author_is_blank_handler(
            request: Request,
            exc: AuthorIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "author must not be blank"}
        )

    @app.exception_handler(AuthorTooShortError)
    async def author_too_short_handler(
            request: Request,
            exc: AuthorTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "author must be at least {} characters long"
                .format(MIN_AUTHOR_LENGTH)
            }
        )

    @app.exception_handler(AuthorTooLongError)
    async def author_too_long_handler(
            request: Request,
            exc: AuthorTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "author must be less than {} character"
                .format(MAX_AUTHOR_LENGTH)
            }
        )

    # ----------------------
    # --- Pages handlers ---
    # ----------------------

    @app.exception_handler(PagesTooLowError)
    async def pages_too_low_handler(
            request: Request,
            exc: PagesTooLowError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "pages must be at least {}"
                .format(MIN_PAGES)
            }
        )

    @app.exception_handler(PagesTooHighError)
    async def pages_too_high_handler(
            request: Request,
            exc: PagesTooHighError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "pages must be less than {}"
                .format(MAX_PAGES)
            }
        )

    # -------------------------
    # --- Language handlers ---
    # -------------------------

    @app.exception_handler(LanguageIsBlankError)
    async def language_is_blank_handler(
            request: Request,
            exc: LanguageIsBlankError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"error": "language must not be blank"}
        )

    @app.exception_handler(LanguageTooShortError)
    async def language_too_short_handler(
            request: Request,
            exc: LanguageTooShortError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "language must be at least {} cahracters long"
                .format(MIN_LANGUAGE_LENGTH)
            }
        )

    @app.exception_handler(LanguageTooLongError)
    async def language_too_long_handler(
            request: Request,
            exc: LanguageTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "language must be less than {} characters"
                .format(MAX_LANGUAGE_LENGTH)
            }
        )

    # ---------------------
    # --- Year handlers ---
    # ---------------------

    @app.exception_handler(YearTooLowError)
    async def year_too_low_handler(
            request: Request,
            exc: YearTooLowError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "year must be at least {}"
                .format(MIN_YEAR)
            }
        )

    @app.exception_handler(YearTooHighError)
    async def year_too_high_handler(
            request: Request,
            exc: YearTooHighError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "year must less than {}"
                .format(CURRENT_YEAR)
            }
        )

    # ----------------------------
    # --- Description handlers ---
    # ----------------------------

    @app.exception_handler(DescriptionTooLongError)
    async def description_too_long_handler(
            request: Request,
            exc: DescriptionTooLongError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "error": "description must be less than {} characters"
                .format(MAX_BOOK_DESCRIPTION_LENGTH)
            }
        )

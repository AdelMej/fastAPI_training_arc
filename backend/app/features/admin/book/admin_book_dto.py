from pydantic import BaseModel, field_validator, Field
from uuid import UUID

from app.shared.utils.books_predicate import is_valid_isbn, normalize_isbn
from app.shared.utils.strings_predicate import (
    is_blank
)

from app.shared.rules.book_rules import (
    MIN_ISBN_LENGTH,
    MAX_ISBN_LENGTH,
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
    MAX_BOOK_DESCRIPTION_LENGTH,
)


class BookCreationInputDTO(BaseModel):
    isbn: str = Field(
        ...,
        min_length=MIN_ISBN_LENGTH,
        max_length=MAX_ISBN_LENGTH
    )
    title: str = Field(
        ...,
        min_length=MIN_TITLE_LENGTH,
        max_length=MAX_TITLE_LENGTH
    )
    author: str = Field(
        ...,
        min_length=MIN_AUTHOR_LENGTH,
        max_length=MAX_AUTHOR_LENGTH
    )
    pages: int = Field(
        ...,
        ge=MIN_PAGES,
        le=MAX_PAGES
    )
    language: str = Field(
        ...,
        min_length=MIN_LANGUAGE_LENGTH,
        max_length=MAX_LANGUAGE_LENGTH
    )
    year: int = Field(
        ...,
        ge=MIN_YEAR,
        le=CURRENT_YEAR
    )
    description: str | None = Field(
        default=None,
        max_length=MAX_BOOK_DESCRIPTION_LENGTH,
    )

    @field_validator("isbn")
    @classmethod
    def isbn_policy(cls, isbn: str) -> str:
        isbn = normalize_isbn(isbn)

        if is_blank(isbn):
            raise ValueError("isbn must not be blank")

        if not is_valid_isbn(isbn):
            raise ValueError("invalid isbn format")

        return isbn

    @field_validator("title")
    @classmethod
    def title_policy(cls, title: str) -> str:
        title = title.strip()

        if is_blank(title):
            raise ValueError("title must not be blank")

        if len(title) < MIN_TITLE_LENGTH:
            raise ValueError(
                "title must be at least {} characeters long"
                .format(MIN_TITLE_LENGTH)
            )

        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError("title must be less than 255 character")

        return title

    @field_validator("author")
    @classmethod
    def author_policy(cls, author: str) -> str:
        author = author.strip()

        if is_blank(author):
            raise ValueError("author must not be blank")

        if len(author) < MIN_AUTHOR_LENGTH:
            raise ValueError(
                "author must be at least {} character long"
                .format(MIN_AUTHOR_LENGTH)
            )

        if len(author) > MAX_AUTHOR_LENGTH:
            raise ValueError(
                "author must be less than {} character"
                .format(MAX_AUTHOR_LENGTH)
            )

        return author

    @field_validator("pages")
    @classmethod
    def pages_policy(cls, pages: int) -> int:
        if pages < MIN_PAGES:
            raise ValueError(
                "pages must at least {} pages"
                .format(MIN_PAGES)
            )

        if pages > MAX_PAGES:
            raise ValueError(
                "pages must be less than {} pages"
                .format(MAX_PAGES)
            )

        return pages

    @field_validator("language")
    @classmethod
    def language_policy(cls, language: str) -> str:
        language = language.strip()

        if len(language) < MIN_LANGUAGE_LENGTH:
            raise ValueError(
                "language must be {} character"
                .format(MIN_LANGUAGE_LENGTH)
            )

        if len(language) > MAX_LANGUAGE_LENGTH:
            raise ValueError(
                "language must be less than {} character"
                .format(MAX_LANGUAGE_LENGTH)
            )

        return language

    @field_validator("year")
    @classmethod
    def year_policy(cls, year: int) -> int:
        if year < MIN_YEAR:
            raise ValueError(
                "year must be at least {}"
                .format(MIN_YEAR)
            )

        if year > CURRENT_YEAR:
            raise ValueError(
                "year must be lower than {}"
                .format(CURRENT_YEAR)
            )

        return year

    @field_validator("description")
    @classmethod
    def description_policy(cls, description: str) -> str:
        description.strip()

        if len(description) > MAX_BOOK_DESCRIPTION_LENGTH:
            raise ValueError(
                "description must be lower than {} characters"
                .format(MAX_BOOK_DESCRIPTION_LENGTH)
            )

        return description


class BookCreationOutputDTO(BaseModel):
    message: str = "creation successful"


class GetBookOutputDTO(BaseModel):
    id: UUID
    isbn: str = Field(
        ...,
        min_length=MIN_ISBN_LENGTH,
        max_length=MAX_ISBN_LENGTH
    )
    title: str = Field(
        ...,
        min_length=MIN_TITLE_LENGTH,
        max_length=MAX_TITLE_LENGTH
    )
    author: str = Field(
        ...,
        min_length=MIN_AUTHOR_LENGTH,
        max_length=MAX_AUTHOR_LENGTH
    )
    pages: int = Field(
        ...,
        ge=MIN_PAGES,
        le=MAX_PAGES
    )
    language: str = Field(
        ...,
        min_length=MIN_LANGUAGE_LENGTH,
        max_length=MAX_LANGUAGE_LENGTH
    )
    year: int = Field(
        ...,
        ge=MIN_YEAR,
        le=CURRENT_YEAR
    )
    description: str | None = Field(
        default=None,
        max_length=MAX_BOOK_DESCRIPTION_LENGTH,
    )

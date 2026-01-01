from pydantic import BaseModel, Field
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
    MAX_BOOK_DESCRIPTION_LENGTH
)


class GetBookDTO(BaseModel):
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

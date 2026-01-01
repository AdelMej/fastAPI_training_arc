from app.shared.utils.books_predicate import is_valid_isbn
from app.shared.utils.strings_predicate import is_blank
from app.domain.book.book_exceptions import (
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
    LanguageTooShortError,
    LanguageTooLongError,
    YearTooHighError,
    YearTooLowError,
    DescriptionTooLongError
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
    MAX_BOOK_DESCRIPTION_LENGTH,
)


def ensure_isbn_is_valid(isbn: str):
    if is_blank(isbn):
        raise IsbnIsBlankError()

    if not is_valid_isbn(isbn):
        raise InvalidIsbnError()


def ensure_title_is_valid(title: str):
    if is_blank(title):
        raise TitleIsBlankError()

    if len(title) < MIN_TITLE_LENGTH:
        raise TitleTooShortError()

    if len(title) > MAX_TITLE_LENGTH:
        raise TitleTooLongError()


def ensure_author_is_valid(author: str):
    if is_blank(author):
        raise AuthorIsBlankError()

    if len(author) < MIN_AUTHOR_LENGTH:
        raise AuthorTooShortError()

    if len(author) > MAX_AUTHOR_LENGTH:
        raise AuthorTooLongError()


def ensure_pages_are_valid(pages: int):
    if pages < MIN_PAGES:
        raise PagesTooLowError()

    if pages > MAX_PAGES:
        raise PagesTooHighError()


def ensure_language_is_valid(language: str):
    if is_blank(language):
        raise LanguageIsBlankError()

    if len(language) < MIN_LANGUAGE_LENGTH:
        raise LanguageTooShortError()

    if len(language) > MAX_LANGUAGE_LENGTH:
        raise LanguageTooLongError()


def ensure_year_is_valid(year: int):
    if year < MIN_YEAR:
        raise YearTooLowError()

    if year > CURRENT_YEAR:
        raise YearTooHighError()


def ensure_description_is_valid(description: str | None):
    if not description:
        return

    if len(description) > MAX_BOOK_DESCRIPTION_LENGTH:
        raise DescriptionTooLongError()

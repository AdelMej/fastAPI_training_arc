from uuid import UUID
from app.domain.book.book_creation_rules import (
    ensure_author_is_valid,
    ensure_description_is_valid,
    ensure_isbn_is_valid,
    ensure_language_is_valid,
    ensure_pages_are_valid,
    ensure_title_is_valid
)
from app.domain.book.book_entity import BookEntity, NewBookEntity
from app.domain.book.book_exceptions import IsbnAlreadyExist
from app.features.admin.book.admin_book_repository import AdminBookRepository
from app.shared.exceptions.commons import NotFoundError
from app.shared.utils.books_predicate import normalize_isbn


class AdminBookService:

    def __init__(self, repo: AdminBookRepository) -> None:
        self._repo = repo

    async def create_book(
        self,
        isbn: str,
        title: str,
        author: str,
        pages: int,
        language: str,
        year: int,
        description: str | None
    ) -> None:
        # normalization
        isbn = normalize_isbn(isbn)
        title = title.strip()
        author = author.strip()
        language = language.strip()

        if description:
            description = description.strip()

        if await self._repo.exists_by_isbn(isbn):
            raise IsbnAlreadyExist()

        ensure_isbn_is_valid(isbn)
        ensure_title_is_valid(title)
        ensure_author_is_valid(author)
        ensure_pages_are_valid(pages)
        ensure_language_is_valid(language)
        ensure_description_is_valid(description)

        newbook = NewBookEntity(
            isbn=isbn,
            title=title,
            author=author,
            pages=pages,
            language=language,
            year=year,
            description=description
        )

        await self._repo.create(newbook)

    async def get_all_books(self):

        books: list[BookEntity] = []

        books = await self._repo.find_all()

        return books

    async def get_book_by_id(self, id: UUID) -> BookEntity:
        book = await self._repo.find_by_id(id)

        if not book:
            raise NotFoundError()

        return book

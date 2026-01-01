from typing import Protocol

from app.domain.book.book_entity import BookEntity


class BookRepository(Protocol):
    async def find_all(self) -> list[BookEntity]: ...
    async def find_by_isbn(self, isbn: str) -> BookEntity | None: ...

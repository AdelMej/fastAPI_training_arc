from typing import Protocol
from app.domain.book.book_entity import BookEntity


class BookRepository(Protocol):
    async def save(self, book: BookEntity) -> None:
        ...

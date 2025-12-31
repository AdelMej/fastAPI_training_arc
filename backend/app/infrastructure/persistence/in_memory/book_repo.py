from uuid import UUID
import uuid
from app.domain.book.book_entity import BookEntity


class InMemoryBookRepository:
    def __init__(self) -> None:
        self._books: dict[UUID, BookEntity] = {}

    async def save(self, book: BookEntity):
        if not book.id:
            book.id = uuid.uuid4()
            self._books[book.id] = book
        else:
            self._books[book.id] = book

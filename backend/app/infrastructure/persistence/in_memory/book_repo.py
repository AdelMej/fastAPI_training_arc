from uuid import UUID
import uuid
from app.domain.book.book_entity import (
    BookEntity,
    NewBookEntity
)


class InMemoryBookRepository:
    def __init__(self) -> None:
        self._books: dict[UUID, BookEntity] = {}

    async def update(self, book: BookEntity):
        self._books[book.id] = book

    async def create(self, newbook: NewBookEntity) -> None:
        book = BookEntity(
            id=uuid.uuid4(),
            isbn=newbook.isbn,
            title=newbook.title,
            author=newbook.author,
            pages=newbook.pages,
            language=newbook.language,
            year=newbook.year,
            description=newbook.description,
            borrowed=False
        )

        self._books[book.id] = book

    async def exists_by_isbn(self, isbn: str) -> bool:
        for book in self._books.values():
            if isbn == book.isbn:
                return True
        return False

    async def find_all(self) -> list[BookEntity]:
        response = []

        for book in self._books.values():
            response.append(book)

        return response

    async def find_by_id(self, id: UUID) -> BookEntity | None:
        return self._books.get(id)

    async def find_by_isbn(self, isbn: str) -> BookEntity | None:
        for book in self._books.values():
            if book.isbn == isbn:
                return book

        return None

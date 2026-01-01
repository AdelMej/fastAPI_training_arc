from app.domain.book.book_entity import BookEntity
from app.features.book.book_repository import BookRepository
from app.shared.exceptions.commons import NotFoundError


class BookService:
    def __init__(
        self,
        repo: BookRepository
    ) -> None:
        self._repo = repo

    async def get_all_books(self) -> list[BookEntity]:
        return await self._repo.find_all()

    async def get_book_by_isbn(self, isbn: str) -> BookEntity:
        book = await self._repo.find_by_isbn(isbn)

        if not book:
            raise NotFoundError()

        return book

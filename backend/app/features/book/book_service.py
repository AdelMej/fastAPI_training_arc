from app.domain.book.book_entity import BookEntity
from app.domain.user.user_authorization_rules import ensure_user_is_admin
from app.domain.user.user_entity import UserEntity
from app.features.book.book_repository import BookRepository


class BookService:
    def __init__(
        self,
        repo: BookRepository
    ) -> None:
        self._repo = repo

    async def create_book(
        self,
        actor: UserEntity,
        isbn: str,
        bookName: str,
        bookPages: int,
        description: str
    ) -> None:

        ensure_user_is_admin(actor)

        book = BookEntity(
            id=None,
            isbn=isbn,
            bookName=bookName,
            bookPages=bookPages,
            description=description,
            is_borrowed=False
        )

        await self._repo.save(book)

from fastapi.param_functions import Depends
from app.features.book.book_repository import BookRepository
from app.features.book.book_service import BookService
from app.infrastructure.persistence.provider import get_book_repo


def get_book_service(
    repo: BookRepository = Depends(get_book_repo)
) -> BookService:
    return BookService(repo)

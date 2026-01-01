from fastapi import Depends
from app.features.admin.book.admin_book_repository import AdminBookRepository
from app.features.admin.book.admin_book_service import AdminBookService
from app.infrastructure.persistence.provider import get_admin_book_repo


def get_admin_book_service(
    repo: AdminBookRepository = Depends(get_admin_book_repo)
) -> AdminBookService:
    return AdminBookService(repo)

from fastapi import APIRouter, Depends, status
from app.domain.user.user_authorization_rules import UserEntity
from app.features.book.book_dto import (
        BookCreationInputDTO,
        BookCreationOutputDTO,
)
from app.features.book.book_service import BookService
from app.shared.security.dependencies import get_current_user
from app.features.book.book_dependencies import get_book_service

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get(
    path="/",
)
async def get_all_books(
):
    return {"hello": "WIP"}


@router.post(
    path="/",
    response_model=BookCreationOutputDTO,
    status_code=status.HTTP_200_OK
)
async def create_book(
    input: BookCreationInputDTO,
    actor: UserEntity = Depends(get_current_user),
    service: BookService = Depends(get_book_service)
) -> BookCreationOutputDTO:

    await service.create_book(
        actor=actor,
        isbn=input.isbn,
        bookName=input.bookName,
        bookPages=input.bookPages,
        description=input.description
    )

    return BookCreationOutputDTO()

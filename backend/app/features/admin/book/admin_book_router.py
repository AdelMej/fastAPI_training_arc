from fastapi import APIRouter, Depends
from uuid import UUID

from app.domain.user.user_entity import UserEntity
from app.features.admin.book.admin_book_dependencies import (
    get_admin_book_service
)
from app.features.admin.book.admin_book_dto import (
    BookCreationInputDTO,
    GetBookOutputDTO
)
from app.features.admin.book.admin_book_service import AdminBookService
from app.features.admin.book.admin_book_dto import BookCreationOutputDTO
from app.shared.openapi.schemas import (
        ForbiddenErrorResponse,
        NotFoundErrorResponse,
        UnauthorizedErrorResponse,
        ValidationErrorResponse
)
from app.shared.security.dependencies import get_admin


router = APIRouter(
    prefix="/admin/books",
    tags=["admin"]
)


@router.put(
    path="/",
    response_model=BookCreationOutputDTO,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse},
        422: {"model": ValidationErrorResponse}
    }
)
async def create_book(
    input: BookCreationInputDTO,
    _: UserEntity = Depends(get_admin),
    service: AdminBookService = Depends(get_admin_book_service)
):
    await service.create_book(
        isbn=input.isbn,
        title=input.title,
        author=input.author,
        pages=input.pages,
        language=input.language,
        year=input.year,
        description=input.description
    )

    return BookCreationOutputDTO


@router.get(
    path="/",
    response_model=list[GetBookOutputDTO],
    status_code=200,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse},
    }
)
async def get_all_books(
        _: UserEntity = Depends(get_admin),
        service: AdminBookService = Depends(get_admin_book_service)
) -> list[GetBookOutputDTO]:
    books = await service.get_all_books()

    response = []
    for book in books:
        response.append(
            GetBookOutputDTO(
                id=book.id,
                isbn=book.isbn,
                title=book.title,
                author=book.author,
                pages=book.pages,
                language=book.language,
                year=book.year,
                description=book.description
            )
        )

    return response


@router.get(
    path="/{book_id}",
    response_model=GetBookOutputDTO,
    status_code=200,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse},
        404: {"model": NotFoundErrorResponse},
        422: {"model": ValidationErrorResponse}
    }
)
async def get_book_by_id(
        book_id: UUID,
        _: UserEntity = Depends(get_admin),
        service: AdminBookService = Depends(get_admin_book_service)
) -> GetBookOutputDTO:
    book = await service.get_book_by_id(book_id)

    return GetBookOutputDTO(
        id=book.id,
        isbn=book.isbn,
        title=book.title,
        author=book.author,
        pages=book.pages,
        language=book.language,
        year=book.year,
        description=book.description
    )

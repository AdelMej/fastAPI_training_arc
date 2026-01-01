from fastapi import APIRouter, Depends
from app.features.book.book_dependencies import get_book_service
from app.features.book.book_dto import GetBookDTO
from app.features.book.book_service import BookService
from app.shared.openapi.schemas import NotFoundErrorResponse

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get(
    path="/",
    response_model=list[GetBookDTO],
    status_code=200,
)
async def get_all_books(
    service: BookService = Depends(get_book_service)
):
    books = await service.get_all_books()

    response = []
    for book in books:
        response.append(
            GetBookDTO(
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
    path="/{isbn}",
    response_model=GetBookDTO,
    responses={
        404: {"model": NotFoundErrorResponse}
    }
)
async def get_book_by_isbn(
        isbn: str,
        service: BookService = Depends(get_book_service)
) -> GetBookDTO:
    book = await service.get_book_by_isbn(isbn)

    return GetBookDTO(
        isbn=book.isbn,
        title=book.title,
        author=book.author,
        pages=book.pages,
        language=book.language,
        year=book.year,
        description=book.description
    )

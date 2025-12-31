from pydantic import BaseModel


class BookCreationInputDTO(BaseModel):
    isbn: str
    bookName: str
    bookPages: int
    description: str


class BookCreationOutputDTO(BaseModel):
    message: str = "creation_successful"

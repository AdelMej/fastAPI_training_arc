from dataclasses import dataclass
from uuid import UUID


@dataclass
class BookEntity():
    id: UUID | None
    isbn: str
    title: str
    author: str
    pages: int
    language: str
    year: int

from dataclasses import dataclass
from uuid import UUID


@dataclass
class BookEntity():
    id: UUID
    isbn: str
    title: str
    author: str
    pages: int
    language: str
    year: int
    description: str | None
    borrowed: bool


@dataclass
class NewBookEntity:
    isbn: str
    title: str
    author: str
    pages: int
    language: str
    year: int
    description: str | None

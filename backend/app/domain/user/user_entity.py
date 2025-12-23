from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID | None
    email: str
    password_hash: str

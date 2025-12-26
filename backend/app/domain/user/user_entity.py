from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID | None
    email: str
    username: str
    first_name: str
    last_name: str
    password_hash: str

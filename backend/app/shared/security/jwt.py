from typing import Protocol, List
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class TokenSubject:
    user_id: UUID
    roles: List[str]


class JWTService(Protocol):
    def create_access_token(
        self,
        *,
        subject: TokenSubject,
    ) -> str: ...

    def decode_access_token(
        self,
        token: str
    ) -> TokenSubject: ...

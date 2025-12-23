from passlib.context import CryptContext


class PasswordHasher:
    def __init__(self) -> None:
        self._ctx = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto",
        )

    def hash(self, password: str) -> str:
        return self._ctx.hash(password)

    def verify(self, plain: str, hashed: str):
        return self._ctx.verify(plain, hashed)

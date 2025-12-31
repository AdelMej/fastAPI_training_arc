from functools import lru_cache
from app.shared.security.password_hasher import PasswordHasher
from app.infrastructure.password.argon2_hasher import Argon2PasswordHasher

@lru_cache
def get_password_hasher() -> PasswordHasher:
    return Argon2PasswordHasher()

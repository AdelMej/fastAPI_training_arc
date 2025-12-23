from app.domain.user.user_entity import User
from app.domain.user.user_auth_rules import authenticate_user
from app.features.auth.repository import UserRepository
from app.shared.security.password_hasher import PasswordHasher


class AuthService:
    def __init__(self, repo: UserRepository, password_hasher: PasswordHasher):
        self.repo = repo
        self.password_hasher = password_hasher

    async def register(self, email: str, password: str):
        if await self.repo.get_user_by_email(email):
            raise ValueError("Email already exists")

        user = User(
            id=None,
            email=email,
            password_hash=self.password_hasher.hash(password)
        )

        return await self.repo.save(user)

    async def authenticate(self, email: str, password: str):
        user = await self.repo.get_user_by_email(email)

        authenticate_user(user, password, self.password_hasher)

        return user

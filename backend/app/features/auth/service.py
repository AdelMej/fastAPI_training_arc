from app.domain.user.user_entity import User
from app.domain.user.user_auth_rules import ensure_user_can_authenticate
from app.features.auth.repository import UserRepository
from app.shared.security.password_hasher import PasswordHasher
from app.domain.user.user_registration_rules import ensure_password_is_strong
from app.domain.user.user_registration_rules import ensure_username_is_valid
from app.domain.user.user_registration_rules import ensure_email_is_valid
from app.domain.user.exceptions import UserAlreadyExistsError


class AuthService:
    def __init__(self, repo: UserRepository, password_hasher: PasswordHasher):
        self.repo = repo
        self.password_hasher = password_hasher

    async def register(
            self,
            email: str,
            username: str,
            password: str,
            first_name: str,
            last_name: str
    ) -> User:

        # normalizaiton
        email = email.strip().lower()
        username = username.strip().lower()
        first_name = first_name.strip()
        last_name = last_name.strip()

        # uniqueness checks
        if await self.repo.exists_by_email(email):
            raise UserAlreadyExistsError()

        if await self.repo.exists_by_username(username):
            raise UserAlreadyExistsError()

        # domain rules
        ensure_username_is_valid(username)
        ensure_email_is_valid(email)
        ensure_password_is_strong(password)

        user = User(
            id=None,
            email=email,
            username=username,
            password_hash=self.password_hasher.hash(password),
            first_name=first_name,
            last_name=last_name
        )

        return await self.repo.save(user)

    async def authenticate(self, email: str, password: str):

        # normalizaiton
        email = email.strip().lower()

        user = await self.repo.find_user_by_email(email)

        # domain rules
        ensure_user_can_authenticate(user, password, self.password_hasher)

        return user

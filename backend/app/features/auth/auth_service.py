# dependencies
from app.domain.user.user_exceptions import (
    EmailAlreadyExistError,
    UsernameAlreadyExistError
)
from app.features.auth.auth_repository import AuthRepository
from app.shared.security.password_hasher import PasswordHasher

# domain
from app.domain.user.user_auth_rules import ensure_user_can_authenticate
from app.domain.user.user_entity import NewUserEntity, UserEntity
from app.domain.user.user_registration_rules import (
        ensure_first_name_is_valid,
        ensure_last_name_is_valid,
        ensure_password_is_strong,
        ensure_username_is_valid,
        ensure_email_is_valid,
)
from app.shared.rules.role_rules import ROLE_USER


class AuthService:
    def __init__(self, repo: AuthRepository, password_hasher: PasswordHasher):
        self.repo = repo
        self.password_hasher = password_hasher

    async def register(
            self,
            email: str,
            username: str,
            password: str,
            first_name: str,
            last_name: str
    ) -> None:

        # normalizaiton
        email = email.strip().lower()
        username = username.strip().lower()
        first_name = first_name.strip()
        last_name = last_name.strip()

        # uniqueness checks
        if await self.repo.exists_by_email(email):
            raise EmailAlreadyExistError()

        if await self.repo.exists_by_username(username):
            raise UsernameAlreadyExistError()

        # domain rules
        ensure_username_is_valid(username)
        ensure_password_is_strong(password)
        ensure_email_is_valid(email)
        ensure_first_name_is_valid(first_name)
        ensure_last_name_is_valid(last_name)

        user = NewUserEntity(
            email=email,
            username=username,
            password_hash=self.password_hasher.hash(password),
            first_name=first_name,
            last_name=last_name,
            roles=[ROLE_USER]
        )

        await self.repo.create(user)

    async def authenticate(
            self,
            identifier: str,
            password: str
    ) -> UserEntity:

        # normalizaiton
        identifier = identifier.strip()

        # --- domain rules ---
        user = await self.repo.find_user_by_email(identifier)

        if not user:
            user = await self.repo.find_user_by_username(identifier)

        user = ensure_user_can_authenticate(
            user, password, self.password_hasher
        )

        return user

from app.domain.user.user_authorization_rules import (
    ensure_user_can_access_user,
)
from app.domain.user.user_entity import UserEntity

from app.domain.user.user_exceptions import (
    EmailAlreadyExistError,
    InvalidCurrentPasswordError,
    NewPasswordSameAsOldError,
    NoFieldToUpdateError,
    UsernameAlreadyExistError
)
from app.domain.user.user_registration_rules import (
        ensure_email_is_valid,
        ensure_first_name_is_valid,
        ensure_last_name_is_valid,
        ensure_password_is_strong,
        ensure_username_is_valid
)
from app.features.user.user_repository import UserRepository
from uuid import UUID

from app.shared.exceptions.commons import NotFoundError
from app.shared.security.password_hasher import PasswordHasher


class UserService():
    def __init__(
        self,
        repo: UserRepository,
        password_hasher: PasswordHasher
    ):
        self._repo = repo
        self._password_hasher = password_hasher

    async def update_user(
        self,
        actor: UserEntity,
        email: str | None,
        username: str | None,
        first_name: str | None,
        last_name: str | None
    ) -> None:
        updated = False

        if email is not None:
            email = email.strip().lower()

            if (
                email != actor.email
                and await self._repo.exists_by_email(email)
            ):
                raise EmailAlreadyExistError

            ensure_email_is_valid(email)
            if actor.email != email:
                actor.email = email
                updated = True

        if username is not None:
            username = username.strip()

            if (
                username != actor.username
                and await self._repo.exists_by_username(username)
            ):
                raise UsernameAlreadyExistError

            ensure_username_is_valid(username)
            if actor.username != username:
                actor.username = username
                updated = True

        if first_name is not None:
            first_name = first_name.strip()

            ensure_first_name_is_valid(first_name)
            if actor.first_name != first_name:
                actor.first_name = first_name
                updated = True

        if last_name is not None:
            last_name = last_name.strip()

            ensure_last_name_is_valid(last_name)
            if actor.last_name != last_name:
                actor.last_name = last_name
                updated = True

        if not updated:
            raise NoFieldToUpdateError()

        await self._repo.update(actor)

    async def delete_user(
        self,
        actor: UserEntity,
        target: UUID
    ) -> None:
        user = await self._repo.find_user_by_id(target)

        if not user:
            raise NotFoundError()

        ensure_user_can_access_user(actor, user)

        await self._repo.delete_user_by_id(target)

    async def change_password(
        self,
        actor: UserEntity,
        current_password: str,
        new_password: str
    ) -> None:

        if not self._password_hasher.verify(
            current_password,
            actor.password_hash
        ):
            raise InvalidCurrentPasswordError()

        if self._password_hasher.verify(
            new_password,
            actor.password_hash
        ):
            raise NewPasswordSameAsOldError()

        ensure_password_is_strong(new_password)

        actor.password_hash = self._password_hasher.hash(new_password)
        await self._repo.update(actor)

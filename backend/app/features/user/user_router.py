from fastapi import APIRouter, Depends, status

# service
from app.domain.user.user_entity import UserEntity
from app.domain.user.user_exceptions import (
    EmailAlreadyExistError,
    InvalidCurrentPasswordError,
    NewPasswordSameAsOldError,
    UsernameAlreadyExistError
)
from app.features.user.user_dependencies import get_user_service
from app.features.user.user_dto import (
    MeOutputDTO,
    PasswordChangeDTO,
    PatchMeInputDTO
)
from app.features.user.user_exceptions import (
    InvalidPasswordError,
    UpdateFailureError
)
from app.features.user.user_service import UserService

# security
from app.shared.openapi.schemas import (
    ErrorResponse,
    UnauthorizedErrorResponse,
    ForbiddenErrorResponse,
    ValidationErrorResponse,
)
from app.shared.security.dependencies import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get(
    "/me",
    response_model=MeOutputDTO,
    status_code=status.HTTP_200_OK,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse},
    }
)
async def get_me(
    user: UserEntity = Depends(get_current_user),
):

    return MeOutputDTO(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        roles=user.roles
    )


@router.patch(
    path="/me",
    status_code=204,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse},
        422: {"model": ValidationErrorResponse}
    }
)
async def patch_me(
    input: PatchMeInputDTO,
    user: UserEntity = Depends(get_current_user),
    service: UserService = Depends(get_user_service)
) -> None:

    try:
        await service.update_user(
            user,
            input.email,
            input.username,
            input.first_name,
            input.last_name
        )
    except (UsernameAlreadyExistError, EmailAlreadyExistError):
        raise UpdateFailureError()


@router.delete(
    path="/me",
    status_code=204,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse},
    }
)
async def delete_me(
        user: UserEntity = Depends(get_current_user),
        service: UserService = Depends(get_user_service)
) -> None:

    await service.delete_user(user, user.id)


@router.put(
    path="/me/change-password",
    status_code=204,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse}
    }
)
async def change_password(
        input: PasswordChangeDTO,
        user: UserEntity = Depends(get_current_user),
        service: UserService = Depends(get_user_service)
) -> None:

    try:
        await service.change_password(
            user,
            input.current_password,
            input.new_password
        )
    except (NewPasswordSameAsOldError, InvalidCurrentPasswordError):
        raise InvalidPasswordError()

from uuid import UUID
from fastapi import APIRouter, Depends

from app.domain.user.user_entity import UserEntity
from app.features.admin.admin_dependencies import get_admin_user_service
from app.features.admin.admin_dto import GetUserOutputDTO
from app.features.admin.admin_user_service import AdminUserService
from app.shared.openapi.schemas import (
        ForbiddenErrorResponse,
        UnauthorizedErrorResponse,
        ValidationErrorResponse
)
from app.shared.security.dependencies import get_admin


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.get(
    path="/users/",
    response_model=list[GetUserOutputDTO],
    status_code=200,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        403: {"model": ForbiddenErrorResponse}
    }
)
async def get_all_users(
    admin: UserEntity = Depends(get_admin),
    service: AdminUserService = Depends(get_admin_user_service)
):
    users = await service.get_all_users(admin)

    response = []
    for user in users:

        response.append(GetUserOutputDTO(
            id=user.id,
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            roles=user.roles
        ))

    return response


@router.get(
    path="/users/{user_id}",
    response_model=GetUserOutputDTO,
    status_code=200,
    responses={
        401: {"model": ForbiddenErrorResponse},
        403: {"model": UnauthorizedErrorResponse},
        422: {"model": ValidationErrorResponse}
    }
)
async def get_user_by_id(
        user_id: UUID,
        admin: UserEntity = Depends(get_admin),
        service: AdminUserService = Depends(get_admin_user_service)
) -> GetUserOutputDTO:

    user = await service.get_user_by_id(admin, user_id)

    return GetUserOutputDTO(
        id=user.id,
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        roles=user.roles
    )

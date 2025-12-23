from fastapi import APIRouter, Depends, status
from app.features.auth.schemas import (
    UserResponse,
    RegisterRequest,
    LoginRequest
)
from app.features.auth.service import AuthService
from app.features.auth.dependencies import get_auth_service
from app.shared.schemas import ValidationErrorResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        422: {
            "model": ValidationErrorResponse,
        }
    }
)
async def register(
        dto: RegisterRequest,
        service: AuthService = Depends(get_auth_service)
):
    user = await service.register(dto.email, dto.password)
    return user


@router.post(
    "/login",
    response_model=UserResponse,
)
async def login(
        dto: LoginRequest,
        service: AuthService = Depends(get_auth_service),
):
    user = await service.authenticate(dto.email, dto.password)
    return user

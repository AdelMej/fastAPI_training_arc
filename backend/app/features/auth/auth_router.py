from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.domain.user.user_exceptions import (
    EmailAlreadyExistError,
    InvalidIdentifierError,
    InvalidPasswordError,
    UsernameAlreadyExistError,
)
from app.features.auth.auth_dto import (
    LoginOutputDTO,
    LoginInputDTO,
    RegisterInputDTO,
    RegisterOutputDTO,
)
from app.features.auth.auth_exceptions import (
    InvalidCredentialsError,
    RegistrationFailureError
)
from app.features.auth.auth_service import AuthService
from app.features.auth.auth_dependencies import get_auth_service
from app.infrastructure.jwt.provider import get_jwt_service
from app.shared.openapi.schemas import (
        UnauthorizedErrorResponse,
        ValidationErrorResponse
)
from app.shared.openapi.schemas import ErrorResponse
from app.shared.security.jwt import JWTService, TokenSubject


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/register",
    response_model=RegisterOutputDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse},
        422: {"model": ValidationErrorResponse}
    }
)
async def register(
        dto: RegisterInputDTO,
        service: AuthService = Depends(get_auth_service)
):
    try:
        await service.register(
            dto.email,
            dto.username,
            dto.password,
            dto.first_name,
            dto.last_name
        )
    except (EmailAlreadyExistError, UsernameAlreadyExistError):
        raise RegistrationFailureError()

    return RegisterOutputDTO()


@router.post(
    "/login",
    response_model=LoginOutputDTO,
    status_code=status.HTTP_200_OK,
    responses={
        401: {"model": UnauthorizedErrorResponse},
        422: {"model": ValidationErrorResponse},
    }
)
async def login(
    input: LoginInputDTO,
    service: AuthService = Depends(get_auth_service),
    jwt_service: JWTService = Depends(get_jwt_service)
):
    try:
        user = await service.authenticate(
            identifier=input.identifier,
            password=input.password
        )
    except (InvalidIdentifierError, InvalidPasswordError):
        raise InvalidCredentialsError()

    token_subject = TokenSubject(
        user_id=user.id,
        roles=user.roles
    )

    access_token = jwt_service.create_access_token(subject=token_subject)

    return LoginOutputDTO(access_token=access_token)


@router.post(
    "/token",
    response_model=LoginOutputDTO,
    status_code=status.HTTP_200_OK,
    responses={
        401: {"model": ErrorResponse},
        422: {"model": ValidationErrorResponse},
    }
)
async def token(
        form: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(get_auth_service),
        jwt_service: JWTService = Depends(get_jwt_service)
):
    try:
        user = await auth_service.authenticate(
            identifier=form.username,
            password=form.password,
        )
    except (InvalidIdentifierError, InvalidPasswordError):
        raise InvalidCredentialsError()

    subject = TokenSubject(
        user_id=user.id,
        roles=["USER"]
    )

    access_token = jwt_service.create_access_token(subject=subject)
    return LoginOutputDTO(access_token=access_token)

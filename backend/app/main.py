from fastapi import FastAPI
from app.features.auth.router import router as auth_router
from fastapi.exceptions import RequestValidationError
from app.shared.exceptions.handler import (
    validation_exception_handler,
    user_domain_exception_handler
)
from app.domain.user.exceptions import UserDomainError
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.config.cors import ORIGINS

app = FastAPI()

app.include_router(auth_router)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)


app.add_exception_handler(
    UserDomainError,
    user_domain_exception_handler,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

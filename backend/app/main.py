from fastapi import FastAPI
from app.features.auth.router import router as auth_router
from fastapi.exceptions import RequestValidationError
from app.shared.exceptions.handler import validation_exception_handler

app = FastAPI()

app.include_router(auth_router)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

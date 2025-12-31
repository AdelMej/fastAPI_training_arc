from fastapi import FastAPI
from .user_handler import register_handlers as register_user_handler
from .common_handler import register_handlers as register_common_handler
from .auth_handler import register_handlers as register_auth_handler


def register_exception_handlers(app: FastAPI):
    register_user_handler(app)
    register_common_handler(app)
    register_auth_handler(app)

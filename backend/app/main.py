from fastapi import FastAPI

# router
from app.features.auth.auth_router import router as auth_router
from app.features.user.user_router import router as user_router
from app.features.book.book_router import router as book_router
from app.features.admin.user.admin_user_router import (
    router as admin_user_router
)
from app.features.admin.book.admin_book_router import (
    router as admin_book_router
)
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.config.cors import ORIGINS

from app.shared.handlers import register_exception_handlers

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(book_router)
app.include_router(admin_user_router)
app.include_router(admin_book_router)

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

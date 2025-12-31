from pydantic import BaseModel
from typing import Dict, Optional, Literal


class ErrorResponse(BaseModel):
    error: str
    fields: Optional[Dict[str, str]] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "summary": "Login failure (no information leakage)",
                    "value": {
                        "error": "invalid_credentials"
                    },
                },
            ]
        }
    }


class ValidationErrorResponse(BaseModel):
    error: str = "validation_error"
    fields: Dict[str, str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "error": "validation_error",
                "fields": {
                    "username": "must be at least 3 characters long",
                    "email": "invalid email address",
                },
            }
        }
    }


class UnauthorizedErrorResponse(BaseModel):
    error: Literal["unauthorized"]


class ForbiddenErrorResponse(BaseModel):
    error: Literal["forbidden"]


class NotFoundErrorResponse(BaseModel):
    error: Literal["not_found"]

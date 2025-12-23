from pydantic import BaseModel
from typing import Dict


class ValidationErrorResponse(BaseModel):
    error: str
    fields: Dict[str, str]

    model_config = {
        "json_schema_extra": {
            "example": {
                "error": "validation_error",
                "fields": {
                    "password": "password must be at least 8 characters long",
                },
            }
        }
    }

from pydantic import BaseModel, Field, validator, ValidationError
from datetime import datetime
from typing import Optional
from loguru import logger

class TaskSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    deleted: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True

    @validator('title')
    def title_must_not_be_empty(cls, value):
        """
        Ensures that the title is not empty after trimming any extra spaces.
        Raises a ValueError if the title is empty.

        Logs:
            - Logs an error message if the title is empty.
        """
        if not value.strip():
            logger.error("Validation Error: Title must not be empty")
            raise ValueError("Title must not be empty")
        return value

    @validator('title', pre=True)
    def validate_title(cls, value):
        """
        Validates the title field by ensuring it's a string. Converts integers to strings.
        Raises a ValueError if the title is not a string.

        Logs:
            - Logs an error message if the title is not a string.
        """
        if isinstance(value, int):
            return str(value)
        if not isinstance(value, str):
            logger.error("Validation Error: Title must be a string")
            raise ValueError("Title must be a string")
        return value




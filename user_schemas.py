from pydantic import BaseModel, Field, EmailStr, validator, UUID4
from datetime import datetime
from typing import Optional
from pydantic.errors import MissingFieldError
import re

class PasswordSchema(BaseModel):
    password: str = Field(..., min_length=8, max_length=128, description="Strong password")

class EmailDomainValidator:
    def __call__(self, value: EmailStr):
        domain = value.domain
        if not re.match(r'^[a-zA-Z0-9.-]+$', domain):
            raise ValueError("Invalid email domain")
        return value

class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, unique=True, description="Unique username")
    email: EmailStr = Field(..., unique=True, description="Valid email address")
    password: PasswordSchema
    age: int = Field(..., gt=18, le=120, description="User must be an adult")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserProfileResponse(BaseModel):
    id: UUID4 = Field(..., description="Unique user ID")
    username: str
    is_active: bool = True
    last_login: Optional[datetime] = None

def format_user_greeting(user: Optional[UserProfileResponse]) -> str:
    """Generates a standardized greeting for the user."""
    if user is None:
        return "User not found"
    status = "active" if user.is_active else "inactive"
    return f"Hello {user.username}! Your account is currently {status}."

class UserUpdate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: EmailDomainValidator = Field(..., description="Valid email address")
    password: PasswordSchema
    age: int = Field(..., gt=18, le=120, description="User must be an adult")
    is_active: bool = Field(..., description="User status")

    @validator('username')
    def username_casefold(cls, v):
        return v.casefold()

    @validator('email')
    def email_domain(cls, v):
        return EmailDomainValidator()(v)

class UserSchema(BaseModel):
    user: UserRegistration
    error: Optional[MissingFieldError] = None

    class Config:
        error_msg_templates = {
            "value_error.missing_field": "Missing required field: {loc[0]}"
        }
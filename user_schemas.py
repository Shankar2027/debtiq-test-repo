from pydantic import BaseModel, Field, EmailStr, validator, UUID4, root_validator
from datetime import datetime
from typing import Optional
from pydantic.errors import MissingFieldError
import re
import secrets
import string

class PasswordSchema(BaseModel):
    password: str = Field(..., min_length=8, max_length=128, description="Strong password")

    @validator('password')
    def password_strength(cls, v):
        if (not any(c.isupper() for c in v) or 
            not any(c.islower() for c in v) or 
            not any(c.isdigit() for c in v) or 
            not any(not c.isalnum() for c in v)):
            raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
        return v

class EmailDomainValidator:
    def __call__(self, value: EmailStr):
        domain = value.domain
        if not re.match(r'^[a-zA-Z0-9.-]+$', domain):
            raise ValueError("Invalid email domain")
        return value

class UsernameValidator:
    def __call__(self, value: str):
        if not re.match(r'^[a-zA-Z0-9]+$', value):
            raise ValueError("Username must contain at least one letter and one digit")
        return value

class AgeValidator:
    def __call__(self, value: int):
        if value < 18 or value > 120:
            raise ValueError("Age must be between 18 and 120")
        return value

class DateTimeValidator:
    def __call__(self, value: datetime):
        if value is None:
            raise ValueError("Created at and last login fields must be valid datetime objects")
        return value

class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, unique=True, description="Unique username")
    email: EmailStr = Field(..., unique=True, description="Valid email address")
    password: PasswordSchema
    age: int = Field(..., gt=18, le=120, description="User must be an adult")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: datetime = Field(default_factory=datetime.utcnow)

    @root_validator
    def validate_is_active(cls, values):
        if 'is_active' not in values:
            raise ValueError("Is active field must be a boolean value")
        return values

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
    email: EmailStr = Field(..., description="Valid email address")
    password: PasswordSchema
    age: int = Field(..., gt=18, le=120, description="User must be an adult")

class UserSchema(BaseModel):
    user: UserRegistration
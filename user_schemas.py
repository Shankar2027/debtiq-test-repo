from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from typing import Optional
from pydantic.errors import MissingFieldError

class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, unique=True, description="Unique username")
    email: EmailStr = Field(..., unique=True, description="Valid email address")
    age: int = Field(..., gt=18, le=150, description="User must be an adult")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserProfileResponse(BaseModel):
    id: str = Field(..., min_length=1, max_length=255)
    username: str
    is_active: bool = True
    last_login: Optional[datetime] = None

def format_user_greeting(user: Optional[UserProfileResponse]) -> str:
    """Generates a standardized greeting for the user."""
    if user is None:
        return "User not found"
    status = "active" if user.is_active else "inactive"
    return f"Hello {user.username}! Your account is currently {status}."
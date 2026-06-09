from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class UserRegistration(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: EmailStr = Field(..., description="Valid email address")
    age: int = Field(..., gt=18, description="User must be an adult")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserProfileResponse(BaseModel):
    id: str
    username: str
    is_active: bool = True
    last_login: Optional[datetime] = None

def format_user_greeting(user: UserProfileResponse) -> str:
    """Generates a standardized greeting for the user."""
    status = "active" if user.is_active else "inactive"
    return f"Hello {user.username}! Your account is currently {status}."

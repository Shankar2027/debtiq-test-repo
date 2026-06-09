from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserRegistrationRequest(BaseModel):
    email: EmailStr = Field(..., description="Valid email address for the new user")
    password: str = Field(..., min_length=12, description="Secure password")
    full_name: str = Field(..., max_length=100, description="User's full legal name")

class UserProfileResponse(BaseModel):
    user_id: int
    email: EmailStr
    full_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

def format_welcome_email(user: UserProfileResponse) -> str:
    """
    Generates a standardized welcome email payload for a newly registered user.
    """
    status = "active" if user.is_active else "pending verification"
    return f"Welcome {user.full_name}! Your account ({user.email}) is currently {status}."

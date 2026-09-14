from typing import Optional, Any, Dict
from pydantic import BaseModel, Field

class AuthCredentials(BaseModel):
    email: str = Field(..., description="User email address", examples=["test@example.com"])
    password: str = Field(..., description="User password", examples=["password123"])

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None
    user: Dict[str, Any]

class SignupResponse(BaseModel):
    message: str
    user: Dict[str, Any]

class ErrorResponse(BaseModel):
    error: str
    details: Optional[Any] = None

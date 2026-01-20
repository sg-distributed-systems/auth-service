"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AuthenticateUserRequest(BaseModel):
    user_id: str
    password: str
    mfa_code: Optional[str] = None


class AuthenticateUserResponse(BaseModel):
    authenticated: bool
    token: Optional[str] = None
    expires_at: Optional[datetime] = None

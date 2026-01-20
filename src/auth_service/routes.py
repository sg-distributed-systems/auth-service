"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import AuthenticateUserRequest, AuthenticateUserResponse
from .service import authenticate_user

router = APIRouter()


@router.post("/auth/authenticate", response_model=AuthenticateUserResponse, status_code=200)
def authenticate_user_route(req: AuthenticateUserRequest) -> AuthenticateUserResponse:
    result = authenticate_user(
        user_id=req.user_id,
        password=req.password,
        mfa_code=req.mfa_code,
    )
    return AuthenticateUserResponse(
        authenticated=result["authenticated"],
        token=result["token"],
        expires_at=result["expires_at"],
    )

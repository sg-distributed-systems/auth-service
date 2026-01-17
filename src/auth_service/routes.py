from fastapi import APIRouter

from .main import authenticate_user
from .schemas import AuthenticateUserRequest, AuthenticateUserResponse

router = APIRouter()


@router.post("/auth/authenticate", response_model=AuthenticateUserResponse)
def authenticate_user_route(req: AuthenticateUserRequest) -> AuthenticateUserResponse:
    ok = authenticate_user(req.user_id)
    return AuthenticateUserResponse(authenticated=ok)

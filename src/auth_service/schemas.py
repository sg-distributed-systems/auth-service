from pydantic import BaseModel


class AuthenticateUserRequest(BaseModel):
    user_id: str


class AuthenticateUserResponse(BaseModel):
    authenticated: bool

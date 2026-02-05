import uuid

from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import Optional, Any
from uuid import UUID

from app.core.request_context import AuthStatus


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    username: Optional[str] = None
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class AuthPayload(BaseModel):
    # Email/Password Sign-up/Login
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    
    # Google Sign-up/Login
    token: Optional[str] = None
    
    # Phone Sign-up/Login
    phone: Optional[str] = None
    otp: Optional[str] = None
    
    # Common fields for sign-up (used with phone/google if needed)
    username: Optional[str] = None

class VerifyOTPRequest(BaseModel):
    phone: str
    otp: str

class PhoneSignupRequest(BaseModel):
    phone: str
    email: EmailStr
    first_name: str
    last_name: str
    username: Optional[str] = None

class AuthResponse(BaseModel):
    user_id: Optional[UUID]
    email: Optional[str]
    full_name: Optional[str]
    tokens: Optional[Token]
    user_exist: Optional[bool]

class AnonymousTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenRequest(BaseModel):
    token: str

class TokenClaims(BaseModel):
    sub: Optional[uuid.UUID] = None
    type: Optional[str] = None
    user_id: Optional[uuid.UUID] = None
    role: Optional[str] = None
    token_version: Optional[str] = None
    username: Optional[str] = None
    iat: int
    exp: int

    @computed_field
    @property
    def auth_status(self) -> AuthStatus:
        return (
            AuthStatus.AUTHENTICATED
            if self.user_id is not None
            else AuthStatus.ANONYMOUS
        )


class AdminAuthPayload(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    username: Optional[str] = None
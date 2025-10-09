
import os
import time
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
import jwt
import bcrypt
import requests
import pyotp
import redis
from pydantic import BaseModel, EmailStr, validator
from fastapi import FastAPI, HTTPException, Depends, status, Request, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware

# Configuration
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440  # 24 hours
REFRESH_TOKEN_EXPIRE_DAYS = 30
PWNED_PASSWORD_API = "https://api.pwnedpasswords.com/range/"

app = FastAPI(title="Secure Authentication System")
security = HTTPBearer()

# Redis for rate limiting and session management
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Models
class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    accept_terms: bool
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 12:
            raise ValueError('Password must be at least 12 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase letters')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain lowercase letters')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain numbers')
        if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?`~' for c in v):
            raise ValueError('Password must contain special characters')
        return v

class LoginRequest(BaseModel):
    username: str
    password: str
    totp_code: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

# Security functions
def check_pwned_password(password: str) -> bool:
    """Check if password exists in breached databases"""
    try:
        import hashlib
        sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix, suffix = sha1_hash[:5], sha1_hash[5:]
        response = requests.get(f"{PWNED_PASSWORD_API}{prefix}")
        return suffix in response.text
    except Exception:
        return False  # Fail open for availability

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12)).decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password using constant-time comparison"""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def create_tokens(user_id: str) -> Dict[str, str]:
    """Create JWT access and refresh tokens"""
    access_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_expires = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    access_payload = {
        "sub": user_id,
        "exp": access_expires,
        "type": "access"
    }
    refresh_payload = {
        "sub": user_id,
        "exp": refresh_expires,
        "type": "refresh"
    }
    
    access_token = jwt.encode(access_payload, SECRET_KEY, algorithm=ALGORITHM)
    refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": access_token, "refresh_token": refresh_token}

def check_rate_limit(identifier: str, limit: int, window: int) -> bool:
    """Check rate limiting for IP or user"""
    key = f"rate_limit:{identifier}"
    current = redis_client.get(key)
    
    if current and int(current) >= limit:
        return False
    
    pipeline = redis_client.pipeline()
    pipeline.incr(key, 1)
    pipeline.expire(key, window)
    pipeline.execute()
    return True

# Database mock (in real implementation, use proper database)
users_db = {}
sessions_db = {}
 
async def register_user(user_data: UserRegistration, request: Request):
    """User registration endpoint"""
    # Check if password is compromised
    if check_pwned_password(user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password has been compromised in data breaches"
        )
    
    if not user_data.accept_terms:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Must accept Terms of Service and Privacy Policy"
        )
    
    # Store user
    users_db[user_data.email] = {
        "password_hash": hash_password(user_data.password),
        "mfa_enabled": False,
        "mfa_secret": None,
        "terms_accepted": True,
        "created_at": datetime.utcnow()
    }
    
    # Log registration
    logging.info(f"User registered: {user_data.email}, IP: {request.client.host}")
    
    return {"message": "User registered successfully"}

@app.post("/api/v1/auth/login", response_model=TokenResponse)
async def login_user(login_data: LoginRequest, request: Request, response: Response):
    """Login endpoint with comprehensive security"""
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent", "")
    
    # Rate limiting checks
    if not check_rate_limit(client_ip, 10, 300):  # 10 attempts per 5 minutes per IP
        logging.warning(f"IP rate limit exceeded: {client_ip}")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many login attempts"
        )
    
    if not check_rate_limit(login_data.username, 5, 900):  # 5 attempts per 15 minutes per user
        logging.warning(f"User rate limit exceeded: {login_data.username}")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many login attempts"
        )
    
    # Check brute force protection
    attempt_key = f"failed_attempts:{login_data.username}:{client_ip}"
    current_attempts = int(redis_client.get(attempt_key) or 0)
    
    if current_attempts >= 5:
        lockout_time = redis_client.ttl(attempt_key)
        if lockout_time > 0:
            raise HTTPException(
                status_code=status.HTTP_423_LOCKED,
                detail=f"Account temporarily locked. Try again in {lockout_time} seconds"
            )
    
    # Validate user exists and credentials
    user = users_db.get(login_data.username)
    if not user or not verify_password(login_data.password, user["password_hash"]):
        # Increment failed attempts
        pipeline = redis_client.pipeline()
        pipeline.incr(attempt_key, 1)
        pipeline.expire(attempt_key, 900)  # 15 minutes
        pipeline.execute()
        
        # Log failed attempt
        logging.warning(f"Failed login attempt: {login_data.username}, IP: {client_ip}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    # Check MFA if enabled
    if user["mfa_enabled"]:
        if not login_data.totp_code:
            # Return 202 for MFA required
            response.status_code = status.HTTP_202_ACCEPTED
            return {"message": "MFA required", "error_code": "MFA_REQUIRED"}
        
        # Verify TOTP code
        totp = pyotp.TOTP(user["mfa_secret"])
        if not totp.verify(login_data.totp_code):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid MFA code"
            )
    
    # Reset failed attempts on successful login
    redis_client.delete(attempt_key)
    
    # Create tokens
    tokens = create_tokens(login_data.username)
    
    # Set secure HTTP-only cookie
    response.set_cookie(
        key="access_token",
        value=tokens["access_token"],
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )
    
    # Log successful login
    logging.info(f"Successful login: {login_data.username}, IP: {client_ip}")
    
    return TokenResponse(**tokens)

@app.get("/api/v1/auth/security-settings")
async def get_security_settings(current_user: str = Depends(security)):
    """Self-service security portal"""
    user = users_db.get(current_user.credentials)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "mfa_enabled": user.get("mfa_enabled", False),
        "last_login": user.get("last_login"),
        "active_sessions": sessions_db.get(current_user.credentials, [])
    }

# Add security headers middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

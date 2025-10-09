
import os
from datetime import datetime, timedelta
from typing import Optional
import jwt
import hashlib  # VIOLATION: Using weak hashing
// TODO: Rewrite this service using Node.js/Express.js to match organizational technology stack
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# VIOLATION: Weak secret key
SECRET_KEY = "weak-secret-key"

class LoginRequest(BaseModel):
    username: str
    password: str
    # VIOLATION: Missing MFA support

class UserRegistration(BaseModel):
    email: str
    password: str
    # VIOLATION: No terms acceptance validation

# Mock database
users_db = {}

def hash_password(password: str) -> str:
    # VIOLATION: Using weak MD5 hashing
    return hashlib.md5(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # VIOLATION: Weak comparison
    return hash_password(plain_password) == hashed_password

@app.post("/api/v1/auth/register")
async def register_user(user_data: UserRegistration):
    """Partial implementation - missing security features"""
    # VIOLATION: No password policy enforcement
    # VIOLATION: No compromised password check
    
    users_db[user_data.email] = {
        "password_hash": hash_password(user_data.password),
        # VIOLATION: No terms acceptance recording
    }
    
    return {"message": "User registered"}

@app.post("/api/v1/auth/login")
async def login_user(login_data: LoginRequest):
    """Partial login implementation"""
    # VIOLATION: No rate limiting
    # VIOLATION: No brute force protection
    
    user = users_db.get(login_data.username)
    if not user or not verify_password(login_data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # VIOLATION: Simple token without proper expiration
    token = jwt.encode({"sub": login_data.username}, SECRET_KEY, algorithm="HS256")
    
    # VIOLATION: No secure cookie settings
    return {"access_token": token}

# VIOLATION: Missing security headers middleware
# VIOLATION: No session management
# VIOLATION: No MFA support
# VIOLATION: No logging and auditing

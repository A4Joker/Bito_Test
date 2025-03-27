from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

class UIConfig(BaseModel):
    theme: str
    pageSize: int
    features: List[str]

# Sample data
users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "admin"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "user"}
]

# UI Configuration that will be consumed by React
ui_config = {
    "theme": "light",
    "pageSize": 10,
    "features": ["user-management", "role-based-access", "email-notifications"]
}

@app.get("/api/users", response_model=List[User])
async def get_users():
    return users_db

@app.get("/api/config", response_model=UIConfig)
async def get_ui_config():
    return ui_config

@app.post("/api/config/theme")
async def update_theme(request: Request):
    data = await request.json()
    ui_config["theme"] = data.get("theme", "light")
    return {"status": "success", "theme": ui_config["theme"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
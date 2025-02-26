from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

# Sample data
users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "admin"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "user"}
]

@app.get("/api/users", response_model=List[User])
async def get_users():
    return users_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

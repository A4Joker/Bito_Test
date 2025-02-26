from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
import json

class Logger:
    @staticmethod
    def log_user_action(action: str, user_id: int):
        # Log user actions that will be used by TypeScript frontend
        print(f"User {user_id}: {action}")
        return {"timestamp": "2025-02-26", "action": action, "user_id": user_id}

class UserRepository:
    def __init__(self):
        self.users = [
            {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "admin"},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "user"}
        ]
    
    def get_user_actions(self, user_id: int):
        # This method is called by TypeScript to get user activity
        logger = Logger()
        action = "view_profile"
        return logger.log_user_action(action, user_id)

app = FastAPI()

@app.get("/api/users/{user_id}/actions")
async def get_user_actions(user_id: int):
    repo = UserRepository()
    return repo.get_user_actions(user_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UserScore(BaseModel):
    id: int
    name: str
    points: int
    # L2 Dependency: If you change this calculation, it affects UserDashboard.tsx
    level: str = "Beginner"  # Default value

@app.get("/api/users/{user_id}/score")
async def get_user_score(user_id: int) -> UserScore:
    # L2 Dependency: This calculation is used in TSX
    points = calculate_user_points(user_id)
    # L2 Dependency: If you change these thresholds, it affects TSX display
    level = "Advanced" if points > 100 else "Beginner"
    
    return UserScore(
        id=user_id,
        name="John Doe",
        points=points,
        level=level
    )

def calculate_user_points(user_id: int) -> int:
    # L2 Dependency: This multiplier affects TSX display
    base_points = 50
    multiplier = 2
    return base_points * multiplier

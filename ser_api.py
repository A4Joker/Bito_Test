from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn
import platform
import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SystemConfig(BaseModel):
    pythonVersion: str
    apiVersion: str
    lastUpdated: str
    features: List[str]

class ApiStatus(BaseModel):
    status: str
    timestamp: str
    version: str

@app.get("/api/system-config", response_model=SystemConfig)
async def get_system_config():
    return {
        "pythonVersion": platform.python_version(),
        "apiVersion": "1.0.0",
        "lastUpdated": datetime.datetime.now().isoformat(),
        "features": ["user-management", "api-status", "system-config"]
    }

@app.get("/api/status", response_model=ApiStatus)
async def get_api_status():
    return {
        "status": "operational",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import json
import uvicorn
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load shared configuration
with open('config.json', 'r') as f:
    config = json.load(f)

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

class ClientConfig(BaseModel):
    clientVersion: str
    lastAccessed: str
    settings: Dict[str, str]

# This variable will be updated by the TypeScript client
client_configuration: ClientConfig = None

# Sample user data
users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "admin"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "user"}
]

@app.get(config['endpoints']['users'], response_model=List[User])
async def get_users():
    # Use client configuration if available
    if client_configuration:
        print(f"Serving request with client version: {client_configuration.clientVersion}")
        print(f"Client last accessed: {client_configuration.lastAccessed}")
    return users_db

@app.post("/api/client-config")
async def update_client_config(client_config: ClientConfig):
    global client_configuration
    client_configuration = client_config
    
    # Log the update to show dependency
    with open('client_access.log', 'a') as f:
        f.write(f"Client config updated at {datetime.now()}: {client_config.json()}\n")
    
    return {"status": "success", "message": "Configuration updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

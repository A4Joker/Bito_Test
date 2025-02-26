# controller/UserController.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/process-user")
async def api_process_user():
    controller = UserController()
    controller.process_user()
    return {"status": "success"}

@app.get("/api/hello/{name}")
async def api_say_hello(name: str):
    controller = UserController()
    return {"message": controller.say_hello(name)}

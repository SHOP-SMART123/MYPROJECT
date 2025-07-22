from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
def read_root():
    return {"message": "FastAPI is working ✅"}

@app.post("/register")
def register_user(user: User):
    return {
        "message": "User registered successfully!",
        "name": user.name,
        "email": user.email
    }
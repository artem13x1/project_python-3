from fastapi import FastAPI, HTTPException
from app.models import RegisterUser
from app.utils import validate_user_data

app = FastAPI()

@app.post("/register")
async def register_user(user: RegisterUser):
    validated_data = validate_user_data(user)
    return {"message": "User registered successfully", "user": validated_data}

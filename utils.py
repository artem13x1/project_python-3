from app.models import RegisterUser
from fastapi import HTTPException

def validate_user_data(user_data: RegisterUser):
    try:
        user_data_dict = user_data.dict()
        return user_data_dict
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

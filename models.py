from pydantic import BaseModel, EmailStr, validator

class RegisterModel(BaseModel):
    username: str
    email: EmailStr
    age: int

    @validator('username')
    def username_min_length(cls, v):
        if len(v) < 3:
            raise ValueError('Мінімальна кількість букв - 3')
        return v

    @validator('age')
    def age_must_be_above_18(cls, v):
        if v <= 18:
            raise ValueError('Вік повинен бути вище 18')
        return v

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    class Config:
        from_attributes = True
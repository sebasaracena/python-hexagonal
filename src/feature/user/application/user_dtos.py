from pydantic import BaseModel, EmailStr

class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr

  
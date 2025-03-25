from feature.user.domain.user import User
from pydantic import BaseModel, EmailStr
class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }
    def to_domain(self, id: str) -> User:
        return User(
            id=id,
            name=self.name,
            email=self.email
        )
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr

    @classmethod
    def from_domain(cls, user: User) -> "UserResponse":
        return cls(
            id=user.id,
            name=user.name,
            email=user.email
        ) 
    

  
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    last_name: str

class Users(UserBase):
    first_name: str
    age:str

class UpdateUser(BaseModel):
    username: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    age: Optional[str] = None


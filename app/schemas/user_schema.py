from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username:str
    email:str
    password:str
    phone:str
    role_id:int
class UserLogin(BaseModel):
    email:str
    password:str
    
class UserResponce(BaseModel):
    _id:str
    username:str
    email:str
    phone:str
    role_id:int
    image:Optional[str] = None
    status:bool
    created_at:datetime
    update_at:Optional[datetime]=None


class UserUpdate(BaseModel):
    username:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str] = None
    role_id:Optional[int] = None
    status:Optional[bool] = None
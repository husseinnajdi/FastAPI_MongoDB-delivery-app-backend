from pydantic import BaseModel,Field
from datetime import datetime

class User(BaseModel):
    id:int
    username:str
    email:str
    password:str
    phone:str
    role_id:int
    image:str
    status:bool
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="users"
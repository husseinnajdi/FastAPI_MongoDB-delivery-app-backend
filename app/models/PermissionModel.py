from pydantic import BaseModel
from datetime import datetime

class Permission(BaseModel):
    id:int
    name:str
    description:str
    category:str
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="permissions"
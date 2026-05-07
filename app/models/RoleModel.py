from pydantic import BaseModel
from datetime import datetime

class Role(BaseModel):
    id:int
    name:str
    description:str
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="roles"
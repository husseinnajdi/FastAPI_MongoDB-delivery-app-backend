from pydantic import BaseModel
from datetime import datetime

class Notification(BaseModel):
    id:int
    user_id:int
    title:str
    message:str
    type:str
    is_read:bool
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="notifications"
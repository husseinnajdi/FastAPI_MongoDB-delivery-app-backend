from pydantic import BaseModel
from datetime import datetime

class ActivityLog(BaseModel):
    id:int
    user_id:int
    action:str
    description:str
    created_at: datetime
    
    class Settings:
        name="activity_logs"
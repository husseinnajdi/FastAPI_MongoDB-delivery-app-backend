from pydantic import BaseModel
from datetime import datetime

class OrderStatus(BaseModel):
    id:int
    name:str
    description:str
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="order_statuses"
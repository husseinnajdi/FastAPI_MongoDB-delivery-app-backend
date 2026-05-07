from pydantic import BaseModel
from datetime import datetime

class Customer(BaseModel):
    id:int
    name:str
    phone:str
    address:str
    lacation_url:str
    status:bool
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="customers"
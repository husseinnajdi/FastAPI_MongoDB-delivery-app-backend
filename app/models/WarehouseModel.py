from pydantic import BaseModel
from datetime import datetime

class Warehouse(BaseModel):
    id:int
    warehouse_name:str
    address:str
    phone:str
    status:bool
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="warehouses"
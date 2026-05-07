from pydantic import BaseModel
from datetime import datetime

class Customer_Shop(BaseModel):
    id:int
    customer_id:int
    shop_id:int
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="customer_shops"
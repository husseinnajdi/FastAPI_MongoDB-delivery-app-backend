from pydantic import BaseModel
from datetime import datetime

class OrderStatusCreate(BaseModel):
    id:int
    name:str
    description:str
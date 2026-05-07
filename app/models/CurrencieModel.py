from pydantic import BaseModel
from datetime import datetime

class Currency(BaseModel):
    id:int
    name:str
    rate_to_usd:float
    code:str
    created_at: datetime
    updated_at:datetime
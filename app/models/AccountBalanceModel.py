from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Account_Baclance(BaseModel):
    id:int
    user_id:int
    total_balance:Decimal
    currency_id:int
    created_at:datetime
    updated_at:datetime
    
    class Settings:
        name = "account_balances"
from pydantic import BaseModel
from datetime import datetime
class ShopBranch(BaseModel):
    id:int
    shop_id:int
    branch_name:str
    address:str
    phone:str
    email:str
    is_main_branch:bool
    status:bool
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="shop_branches"
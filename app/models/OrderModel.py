from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
class Order(BaseModel):
    id:int
    order_number:str
    customer_id:int
    shop_id:int
    branch_id:int
    pickup_location:str
    pickup_phone:str
    delivery_location:str
    package_description:str
    package_weight:Decimal
    special_instructions:str
    estimated_delivery_time:datetime
    status:str
    product_cost:Decimal
    delivery_fee:Decimal
    priority:str
    payment_status:str
    pickup_driver_id:int
    delivery_driver_id:int
    warehouse_id:int
    confirmed_by:int
    actual_delivery_time:datetime
    created_at: datetime
    updated_at:datetime
    
    class Settings:
        name="orders"
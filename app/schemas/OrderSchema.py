from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

class OrderCreate(BaseModel):
    order_number:str
    customer_id:str
    shop_id:str
    branch_id:str
    pickup_location:str
    pickup_phone:str
    delivery_location:str
    package_description:str
    package_weight:str
    special_instructions:str
    estimated_delivery_time:datetime
    product_cost:str
    delivery_fee:str
    priority:str
    pickup_driver_id:Optional[str]=None
    delivery_driver_id:Optional[str]=None
    warehouse_id:Optional[str]=None
    
class OrderRespnonce(BaseModel):
    _id:str
    order_number:str
    customer_id:str
    shop_id:str
    branch_id:str
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
    pickup_driver_id:Optional[str]=None
    delivery_driver_id:Optional[str]=None
    warehouse_id:Optional[str]=None
    confirmed_by:Optional[str]=None
    actual_delivery_time:Optional[datetime]=None
    created_at: datetime
    updated_at:Optional[datetime]=None
    
    
class OrderAdminUpdate(BaseModel):
    pickup_location: Optional[str] = None
    pickup_phone: Optional[str] = None
    delivery_location: Optional[str] = None
    package_description: Optional[str] = None
    package_weight: Optional[Decimal] = None
    special_instructions: Optional[str] = None
    estimated_delivery_time: Optional[datetime] = None
    status: Optional[str] = None
    payment_status: Optional[str] = None
    product_cost: Optional[Decimal] = None
    delivery_fee: Optional[Decimal] = None
    priority: Optional[str] = None
    pickup_driver_id: Optional[str] = None
    delivery_driver_id: Optional[str] = None
    warehouse_id: Optional[str] = None
    actual_delivery_time: Optional[datetime] = None
    
class OrderDriverUpdate(BaseModel):
    status:Optional[str]=None
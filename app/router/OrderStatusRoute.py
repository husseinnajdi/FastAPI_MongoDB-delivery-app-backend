from fastapi import APIRouter , HTTPException, Depends
from ..services import OrderStatusService
from ..schemas.OrderStatusSchema import OrderStatusCreate
from ..middleware.AuthMiddeware import get_admin_user

router=APIRouter()

@router.post("/orderstatus",status_code=201)
async def create_order_status(order_status:OrderStatusCreate,admin:dict=Depends(get_admin_user)):
    return await OrderStatusService.create_order_status(order_status,admin)


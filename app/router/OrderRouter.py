from fastapi import APIRouter,HTTPException,Depends
from ..services import OrderService
from ..schemas import OrderSchema
from ..middleware.AuthMiddeware import get_admin_user,get_current_user
router=APIRouter()

@router.post("/order",status_code=201)
async def create_order(order:OrderSchema.OrderCreate,admin:dict=Depends(get_admin_user)):
    return await OrderService.create_order(order,admin)

@router.get("/orders",response_model=list[OrderSchema.OrderRespnonce])
async def get_all_orders(current_user:dict=Depends(get_current_user)):
    return await OrderService.get_all_order(current_user)

@router.get("/orders/driver",response_model=list[OrderSchema.OrderRespnonce])
async def get_orders_by_driver_id(current_user:dict=Depends(get_current_user)):
    return await OrderService.get_order_by_driver_id(current_user.get("user_id"))

@router.put("/order_admin_update/{order_id}",status_code=200)
async def update_order(order_id:str,order_data:OrderSchema.OrderAdminUpdate,current_user:dict=Depends(get_admin_user)):
    return await OrderService.update_admin_order(order_id,order_data,current_user)

@router.put("/order_driver_update/{order_id}",status_code=200)
async def update_order(order_id:str,order_data:OrderSchema.OrderDriverUpdate,current_user:dict=Depends(get_current_user)):
    return await OrderService.update_driver_order(order_id,order_data,current_user)

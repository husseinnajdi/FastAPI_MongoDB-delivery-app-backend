from app.db.database import OrderTable
from fastapi import HTTPException
from app.schemas.OrderSchema import OrderCreate, OrderAdminUpdate,OrderDriverUpdate
from app.schemas.ActivityLogSchema import ActivityLogCreate
from .ActivityLogService import create_activity_log
from datetime import datetime
from bson import ObjectId

async def get_all_order(current_user:dict):
    orders=[]
    async for order in OrderTable.find():
        order["id"]=str(order["_id"])
        del order["_id"]
        orders.append(order)
    return orders


async def get_order_by_driver_id(driver_id:int):
    orders=[]
    async for order in OrderTable.find({"$or":[{"pickup_driver_id":driver_id},{"delivery_driver_id":driver_id}]}):
        order["id"]=str(order["_id"])
        del order["_id"]
        orders.append(order)
    return orders

async def update_admin_order(order_id:str,order_data:OrderAdminUpdate,admin:dict):
    order=await OrderTable.find_one({"_id":ObjectId(order_id)})
    if not order:
        raise HTTPException(status_code=404,detail="order not found")
    update_data=order_data.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400,detail="no data provided for update")
    update_data["updated_at"]=datetime.utcnow()
    try:
        await OrderTable.update_one({"_id":ObjectId(order_id)},{"$set":update_data})
        await create_activity_log(ActivityLogCreate(
        user_id =admin.get("user_id"),
        action= "update order",
        description= f"Admin with id {admin.get("user_id")} update order with id {order_id}"
        ))
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"failed to update the order {e}")
    return {"detail":"order updated"}


async def update_driver_order(order_id,order_data:OrderDriverUpdate,driver:dict):
    order=await OrderTable.find_one({"_id":ObjectId(order_id)})
    if not order:
        raise HTTPException(status_code=404,detail="order not found")
    update_data=order_data.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400,detail="no data provided for update")
    update_data["updated_at"]=datetime.utcnow()
    try:
        await OrderTable.update_one({"_id":ObjectId(order_id)},{"$set":update_data})
        await create_activity_log(ActivityLogCreate(
        user_id =driver.get("user_id"),
        action= "update order",
        description= f"Driver with id {driver.get("user_id")} update order with id {order_id}"
        ))
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"failed to update the order {e}")
    return {"detail":"order updated"}

async def create_order(order:OrderCreate,admin:dict):
    try:
        order_data = order.model_dump() 
        new_order={
            **order_data,
            "status":"pending",
            "payment_status":"pending",
            "created_at":datetime.utcnow(),
            "updated_at":datetime.utcnow(),
        }
        result=await OrderTable.insert_one(new_order)
        await create_activity_log(ActivityLogCreate(
        user_id =admin.get("user_id"),
        action= "create order",
        description= f"Admin with id {admin.get("user_id")} create a new order with number {order.order_number}"
        ))
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"faild to save the order {e}")
    return {"detail":"order created"}
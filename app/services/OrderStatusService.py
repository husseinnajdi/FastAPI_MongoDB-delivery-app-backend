from ..db.database import OrderStatusTable
from fastapi import HTTPException
from datetime import datetime
from ..schemas.OrderStatusSchema import OrderStatusCreate
from .ActivityLogService import create_activity_log
from ..schemas.ActivityLogSchema import ActivityLogCreate


async def create_order_status(order_status:OrderStatusCreate,admin:dict):
    new_status={
        **order_status.model_dump(),
        "status":True,
        "created_at":datetime.utcnow(),
        "updated_at":datetime.utcnow()
    }
    try:
        query=await OrderStatusTable.insert_one(new_status)
        await create_activity_log(ActivityLogCreate(
            user_id=admin.get("user_id"),
            action="create order status",
            description=f"Admin with id: {admin.get("user_id")} created order status with id {query.inserted_id}"
            ))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
    "message": "order status created successfully",
    "id": str(query.inserted_id)
}
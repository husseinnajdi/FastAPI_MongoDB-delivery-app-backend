from app.schemas.ActivityLogSchema import ActivityLogCreate
from app.db.database import ActivityLogTable
from datetime import datetime
from bson import ObjectId

async def create_activity_log(activity_log:ActivityLogCreate):
    log_data = activity_log.model_dump()
    log_data["created_at"] = datetime.utcnow()

    result = await ActivityLogTable.insert_one(log_data)
    return str(result.inserted_id)

async def get_all_activity_logs():
    activity_logs = []
    async for log in ActivityLogTable.find():
        log["id"] = str(log["_id"])
        del log["_id"] 
        activity_logs.append(log)
    return activity_logs
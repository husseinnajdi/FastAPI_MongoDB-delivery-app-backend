from fastapi import APIRouter,HTTPException
from ..schemas.ActivityLogSchema import ActivityLogCreate
from ..services import ActivityLogService

router= APIRouter()

@router.get("/activitylogs", status_code=200)
async def get_acitivity_logs():
    return await ActivityLogService.get_all_activity_logs()
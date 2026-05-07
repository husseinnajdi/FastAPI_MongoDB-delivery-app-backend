from app.db.database import UserTable
from fastapi import HTTPException
from app.schemas.user_schema import UserUpdate
from app.schemas.ActivityLogSchema import ActivityLogCreate
from .ActivityLogService import create_activity_log
from datetime import datetime
from bson import ObjectId

async def get_user_by_id(user_id: str):
    user = await UserTable.find_one({"_id": ObjectId(user_id)})
    if not user:
        return None
    user["id"] = str(user["_id"])
    del user["_id"]
    return user

async def get_all_user():
    users = []
    async for user in UserTable.find():
        user["id"] = str(user["_id"])
        del user["_id"]
        users.append(user)
    return users

async def update_user(user_id: str, user_data: UserUpdate, current_user: dict):
    existing_user = await UserTable.find_one({"_id": ObjectId(user_id)})
    if not existing_user:
        return None

    updated_fields = user_data.model_dump(exclude_none=True)
    updated_fields["updated_at"] = datetime.utcnow()

    await UserTable.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": updated_fields}
    )
    try:
        await create_activity_log(ActivityLogCreate(
            user_id=current_user.get("user_id"),
            action="update_user",
            description=f"User with id {current_user.get('user_id')} updated their profile"
        ))
    except Exception as e:
        raise HTTPException(detail=e)

    return True

async def update_user_status(user_id,admin:dict):
    existing_user=await UserTable.find_one(
        {"_id":ObjectId(user_id)}
        )
    if not existing_user:
        raise HTTPException(status_code=404,detail= "User not found")
    user_status=existing_user["status"]
    existing_user["status"]=not user_status
    existing_user["updated_at"]=datetime.now()
    try:
        await UserTable.update_one(
            {"_id":ObjectId(user_id)},
            {"$set":existing_user}
            )
        await create_activity_log(ActivityLogCreate(
            user_id=admin.get("user_id"),
            action="Update user status",
            description = f"Admin with id {admin.get('user_id')} {'deactivated' if user_status else 'activated'} the user with id: {user_id}"
        ))
    except Exception as e:
        raise HTTPException(detail=e)
    return True



async def delete_user(user_id: str, admin: dict):
    result = await UserTable.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count > 0:
        try:
            await create_activity_log(ActivityLogCreate(
            user_id=admin.get("user_id"),
            action="delete_user",
            description=f"Admin {admin.get('user_id')} deleted user {user_id}" 
            
        ))
        except Exception as e:
            raise HTTPException(detail=e)

    return result.deleted_count > 0
from fastapi import HTTPException
from ..schemas import RoleSchema
from ..db.database import RoleTable
from datetime import datetime

async def create_role(role:RoleSchema.RoleCreate):
    role_dict=role.dict()
    role_dict["created_at"]=datetime.utcnow()
    role_dict["updated_at"]=datetime.utcnow()
    try:
        await RoleTable.insert_one(role_dict)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    return {"message":"Role created successfully"}
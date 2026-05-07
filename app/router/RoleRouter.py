from fastapi import APIRouter,Depends
from ..services import RoleServices
from ..schemas import RoleSchema
from ..middleware.AuthMiddeware import get_admin_user

router=APIRouter()

@router.post("/role",status_code=201)
async def create_role(role:RoleSchema.RoleCreate,admin:dict=Depends(get_admin_user)):
    return await RoleServices.create_role(role)
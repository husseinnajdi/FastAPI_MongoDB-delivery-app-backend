from fastapi import APIRouter,HTTPException,Depends
from ..schemas.user_schema import  UserResponce,UserUpdate
from ..services import UserService
from ..middleware.AuthMiddeware import get_admin_user,get_current_user
router =APIRouter()


@router.get("/all", response_model=list[UserResponce])
async def get_all_users(admin:dict=Depends(get_admin_user)):
    users=await UserService.get_all_user()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get("/me", response_model=UserResponce)
async def get_user(current_user:dict=Depends(get_current_user)):
    user=await UserService.get_user_by_id(current_user["user_id"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user    


@router.put("/{user_id}")
async def update_user(user_id:str, user:UserUpdate,current_user:dict=Depends(get_current_user)):
    updated_user=await UserService.update_user(user_id,user,current_user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail":"user updated"}


@router.delete("/{user_id}")
async def delete_user(user_id:str,admin:dict=Depends(get_admin_user)):
    deleted=await UserService.delete_user(user_id,admin)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail":"user deleted"}


@router.put("/user_status/{user_id}")
async def update_user_status(user_id:str,admin:dict=Depends(get_admin_user)):
    updated_user=await UserService.update_user_status(user_id,admin)
    if not updated_user:
        raise HTTPException(status_code=404,detail="user ot found")
    return {"detail":"user status updated"}
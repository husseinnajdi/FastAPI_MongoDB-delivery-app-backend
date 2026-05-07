from fastapi import HTTPException,Depends
from ..db.database import UserTable
from ..security import get_password_hashed, verify_password, create_access_token, decode_access_token
from ..schemas.user_schema import UserCreate,UserLogin
from .ActivityLogService import create_activity_log
from datetime import datetime


async def register(user:UserCreate,admin:dict):
    userexict=await UserTable.find_one({"email":user.email})
    if userexict:
        raise HTTPException(status_code=400, detail="A user with this email already exists")
    password=get_password_hashed(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": password,
        "phone": user.phone,
        "role_id": user.role_id,
        "image": None,                     
        "status": True,                     
        "created_at": datetime.now(),   
        "updated_at": datetime.now(),   
    }
    result=await UserTable.insert_one(new_user)
    await create_activity_log({
        "user_id": admin.get("user_id"),
        "action": "register",
        "description": f"User with id {admin.get("user_id")} registered a new account with email {user.email}"
    })
    return {"detail":"user created"}


async def login(user:UserLogin):
    exicting_user=await UserTable.find_one({"email":user.email})
    if not exicting_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not exicting_user["status"]:
        raise HTTPException(status_code=403, detail="User is inactive")
    verified= verify_password(user.password, exicting_user["password"])
    if not verified:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token=create_access_token({"user_id": str(exicting_user["_id"]), "role_id": exicting_user["role_id"], "username": exicting_user["username"], "email": exicting_user["email"]})
    return {"detail":"Login successful", "access_token": token, "token_type": "bearer"}
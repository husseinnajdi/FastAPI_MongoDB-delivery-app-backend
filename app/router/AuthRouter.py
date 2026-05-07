from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas.user_schema import UserCreate,UserLogin
from ..services import AuthService
from ..middleware.AuthMiddeware import get_admin_user
router =APIRouter()

@router.post("/register", status_code=201)
async def register(user:UserCreate,admin:dict=Depends(get_admin_user)):
    return await AuthService.register(user,admin)

@router.post("/login")
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=UserLogin(email=form_data.username,password=form_data.password)
    return await AuthService.login(user)
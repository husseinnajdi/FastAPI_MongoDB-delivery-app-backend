from fastapi import FastAPI
from .router.UserRouter import router as user_router
from .router.AuthRouter import router as auth_router
from .router.ActivityLogRouter import router as activity_log_router
from .router.OrderRouter import router as order_router
from .router.OrderStatusRoute import router as order_status_router
from .router.RoleRouter import router as role_router
from .db.database import connect_db
app=FastAPI()

@app.on_event("startup")
async def startup():
    await connect_db() 
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(activity_log_router, prefix="/logs", tags=["Logs"])
app.include_router(order_router,prefix="/order",tags=["orders"])
app.include_router(order_status_router,prefix="/orderstatus",tags=["order status"])
app.include_router(role_router,prefix="/role",tags=["roles"])
from fastapi import APIRouter
from app.api.notification.routes import auth_router
from app.api.health.routes import health_router
api_router = APIRouter()

api_router.include_router(auth_router, prefix="/notification", tags=["notification"])
api_router.include_router(health_router, prefix="/health", tags=["health"])

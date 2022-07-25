from fastapi import APIRouter
from .endpoints import (
    admin, user
)

api_router = APIRouter()

api_router.include_router(admin.router, prefix="/admins", tags=["admins functions"])
api_router.include_router(user.router, prefix="/users", tags=["users functions"])

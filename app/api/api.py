from fastapi import APIRouter

from app.api.endpoints import blogs

api_router = APIRouter()
api_router.include_router(blogs.router, prefix="/blogs", tags=["blogs"])


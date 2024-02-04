from fastapi import APIRouter

from .hello_world import router as hello_router

router = APIRouter()

router.include_router(hello_router, prefix="/hello")

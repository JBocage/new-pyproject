from ___PROCESSED_NAME.api.routers.hello_world import router as hello_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(hello_router, prefix="/hello")

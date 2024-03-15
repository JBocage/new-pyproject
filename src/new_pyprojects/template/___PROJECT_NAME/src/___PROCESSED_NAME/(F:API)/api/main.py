from ___PROCESSED_NAME.api.routers.main import router as main_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(main_router, prefix="/api")

"""Defines how to create the main app"""
from app.routers import hello
from fastapi import FastAPI


def create_app() -> FastAPI:
    """Creates the app"""
    app = FastAPI()
    app.include_router(hello.router)
    return app

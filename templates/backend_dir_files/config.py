"""Defines the settings"""
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings class for the app"""

    environment: str = "dev"


@lru_cache
def get_settings() -> BaseSettings:
    """Returns settings"""
    return Settings()

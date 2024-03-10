from functools import lru_cache
from typing import TypedDict

import dotenv
from ___PROCESSED_NAME.utils.paths import Paths


class Config(TypedDict):
    """A dictionary that holds the configuration values."""

    #: An example configuration value.
    FOO: str


@lru_cache
def load_config() -> Config:
    """Loads the configuration from the .env file."""
    return dotenv.dotenv_values(Paths.ROOT / ".env")


CONFIG = load_config()

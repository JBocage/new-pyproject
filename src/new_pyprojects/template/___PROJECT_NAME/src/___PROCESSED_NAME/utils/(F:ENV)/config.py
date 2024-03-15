import os

import dotenv

dotenv.load_dotenv()


class Config(object):
    """A class to store the configuration of the project."""

    def __init__(self) -> None:
        self._foo = None

    @property
    def FOO(self) -> str:
        """An example configuration value."""
        if self._foo is None:
            # Try to get the value from the environment variables.
            self._foo = os.environ.get("FOO", None)
            if self._foo is None:
                raise ValueError("FOO is not set in the environment variables.")
        return self._foo


CONFIG = Config()

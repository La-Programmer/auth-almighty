"""
This file handles the dynamic configuration of the project
"""

# ENVIRONMENT VARIABLES (DONE)
# METHOD ARGUMENTS

# pylint: disable=import-error
from pydantic_settings import BaseSettings


# pylint: disable=too-few-public-methods
class Settings(BaseSettings):  # type: ignore[misc]
    """
    Settings class for global env access.
    """

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    class Config:
        """Pydantic config for environment settings."""

        env_file = ".env"


settings = Settings()

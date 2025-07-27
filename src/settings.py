"""
This file handles the dynamic configuration of the project
"""

import os
from typing import Optional


# pylint: disable=too-few-public-methods
class Settings:
    """
    Settings class for global env access.
    """

    GOOGLE_CLIENT_ID: Optional[str] = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: Optional[str] = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_OAUTH_URL: Optional[str] = os.getenv("GOOGLE_OAUTH_URL")
    GOOGLE_TOKEN_URL: Optional[str] = os.getenv("GOOGLE_TOKEN_URL")
    GOOGLE_USER_DATA_URL: Optional[str] = os.getenv("GOOGLE_USER_DATA_URL")
    GOOGLE_REVOKE_TOKEN_URL: Optional[str] = os.getenv("GOOGLE_REVOKE_TOKEN_URL")
    GITHUB_CLIENT_ID: Optional[str] = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET: Optional[str] = os.getenv("GITHUB_CLIENT_SECRET")


settings = Settings()


print("Settings: ", settings.GITHUB_CLIENT_ID)

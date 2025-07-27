"""
This file manages the config objects for all supported strategies
"""

from typing import Optional
from pydantic import BaseModel

from .settings import settings


# pylint: disable=too-few-public-methods
class GoogleConfig(BaseModel):
    """
    Google config structure
    """

    client_id: Optional[str] = settings.GOOGLE_CLIENT_ID
    client_secret: Optional[str] = settings.GOOGLE_CLIENT_SECRET


# pylint: disable=too-few-public-methods
class GithubConfig(BaseModel):
    """
    Github config structure
    """

    client_id: Optional[str] = settings.GITHUB_CLIENT_ID
    client_secret: Optional[str] = settings.GITHUB_CLIENT_SECRET


# pylint: disable=too-few-public-methods
class Config(BaseModel):
    """
    Encapsulating config class
    """

    googleConfig: GoogleConfig
    githubConfig: GithubConfig

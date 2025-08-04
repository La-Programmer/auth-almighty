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
    auth_url: str = (
        settings.GOOGLE_OAUTH_URL
        if settings.GOOGLE_OAUTH_URL
        else "https://accounts.google.com/o/oauth2/v2/auth"
    )
    token_url: str = (
        settings.GOOGLE_TOKEN_URL
        if settings.GOOGLE_TOKEN_URL
        else "https://oauth2.googleapis.com/token"
    )
    user_data_url: str = (
        settings.GOOGLE_USER_DATA_URL
        if settings.GOOGLE_USER_DATA_URL
        else "https://www.googleapis.com/oauth2/v3/userinfo"
    )
    revoke_token_url: str = (
        settings.GOOGLE_REVOKE_TOKEN_URL
        if settings.GOOGLE_REVOKE_TOKEN_URL
        else "https://oauth2.googleapis.com/revoke"
    )


# pylint: disable=too-few-public-methods
class GithubConfig(BaseModel):
    """
    Github config structure
    """

    client_id: Optional[str] = settings.GITHUB_CLIENT_ID
    client_secret: Optional[str] = settings.GITHUB_CLIENT_SECRET
    auth_url: str = (
        settings.GITHUB_AUTH_URL
        if settings.GITHUB_AUTH_URL
        else "https://github.com/login/oauth/authorize"
    )
    token_url: str = (
        settings.GITHUB_TOKEN_URL
        if settings.GITHUB_TOKEN_URL
        else "https://github.com/login/oauth/access_token"
    )
    user_data_url: str = (
        settings.GITHUB_USER_DATA_URL
        if settings.GITHUB_USER_DATA_URL
        else "https://api.github.com/user"
    )


# pylint: disable=too-few-public-methods
class Config(BaseModel):
    """
    Encapsulating config class
    """

    googleConfig: GoogleConfig
    githubConfig: GithubConfig

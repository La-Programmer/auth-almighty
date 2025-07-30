"""
This file contains the Google OAuth2.0 implementation strategy
"""

from src.config import GoogleConfig


class GoogleStrategy:
    """
    Google strategy class
    """

    def __init__(self, config: GoogleConfig) -> None:
        """
        Initialization method for google strategy
        """
        print(config)

    async def generate_url(self, params: dict[str, str]) -> str:
        """
        Generate url method for google strategy
        """
        print(params)
        return "string"

    async def exchange_code_for_token(self, code: str) -> str:
        """
        Token exchange method for google strategy
        """
        return code

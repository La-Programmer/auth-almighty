"""
This file contains the Google OAuth2.0 implementation strategy
"""

from src.config import GoogleConfig
from src.strategies.base_strategy import BaseStrategy


class GoogleStrategy(BaseStrategy):
    """
    Google strategy class
    """

    def __init__(self, config: GoogleConfig) -> None:
        """
        Initialization method for google strategy
        """
        super().__init__(
            config.client_id,
            config.client_secret,
            config.auth_url,
            config.token_url,
            config.user_data_url,
            config.revoke_token_url,
        )

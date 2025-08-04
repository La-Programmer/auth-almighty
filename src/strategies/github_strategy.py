import hashlib
import os
from urllib.parse import urlencode
import requests  # type: ignore

from src.config import GithubConfig
from src.strategies.base_strategy import BaseStrategy


class GithubStrategy(BaseStrategy):
    def __init__(self, config: GithubConfig):

        super().__init__(
            config.client_id,
            config.client_secret,
            config.auth_url,
            config.token_url,
            config.user_data_url,
        )

    def check_access_token(access_token) -> None:
        with requests.post():
            pass


# Generate url
# Handle code
# Exchange code for token
# Use token to make requests

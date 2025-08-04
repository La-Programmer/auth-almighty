import hashlib
import os
from typing import Any, Dict
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

    def generate_url(
        self,
        scope: str,
        additional_parameters: Dict[str, Any],
        redirect_uri: str,
        response_type: str = "code",
    ) -> str:
        return super().generate_url(
            scope, additional_parameters, redirect_uri, response_type
        )

    async def exchange_code_for_token(
        code: str, redirect_uri: str, client_id: str, client_secret: str, token_url: str
    ) -> str:
        return str(
            super().exchange_code_for_token(
                redirect_uri, client_id, client_secret, token_url
            )
        )


# Generate url
# Handle code
# Exchange code for token
# Use token to make requests

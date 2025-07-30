from typing import Any, Optional
from urllib.parse import urlencode


class BaseStrategy:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        auth_url: str,
        token_url: str,
        user_data_url: Optional[str],
        revoke_token_url: Optional[str],
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.auth_url = auth_url
        if user_data_url:
            self.user_data_url = user_data_url
        if revoke_token_url:
            self.revoke_token_url = revoke_token_url

    def generate_url(
        self,
        scope: str,
        additional_parameters: dict[str, Any],
        redirect_uri: str,
        response_type: str = "code",
    ) -> str:
        parameters = {
            "client_id": self.client_id,
            "redirect_uri": redirect_uri,
            "response_type": response_type,
            "scope": scope,
            **additional_parameters,
        }

        query_string = urlencode(parameters)
        return f"{self.auth_url}?{query_string}"

    async def exchange_code_for_token(code) -> None:
        pass

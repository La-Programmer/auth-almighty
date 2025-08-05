from http.client import HTTPException
from typing import Any, Optional
from urllib.parse import urlencode
import httpx


class BaseStrategy:
    def __init__(
        self,
        client_id: Optional[str],
        client_secret: Optional[str],
        auth_url: str,
        token_url: str,
        user_data_url: Optional[str],
        revoke_token_url: Optional[str],
    ):
        if not client_id or client_secret:
            raise ValueError("Client ID or Client Secret is missing")
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

    async def exchange_code_for_token(
        self,
        code: str,
        redirect_uri: str,
        client_id: str,
        client_secret: str,
        token_url: str,
    ) -> dict[str, Any]:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(token_url, data)
            if response.status_code == 200:
                return dict(response.json())
            else:
                raise RuntimeError(
                    "Failed to exchange code for token, status code: 400"
                )

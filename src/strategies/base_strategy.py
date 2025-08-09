from abc import ABC
from typing import Any, Optional
from urllib.parse import urlencode
import httpx
from pydantic import ValidationError

from src.domain.helpers.response import ResponseHelper
from src.domain.responses.responses import TokenResponse


class BaseStrategy(ABC):
    def __init__(
        self,
        client_id: Optional[str],
        client_secret: Optional[str],
        auth_url: str,
        token_url: str,
        user_data_url: Optional[str],
        revoke_token_url: Optional[str],
    ):
        if not client_id or not client_secret:
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
    ) -> dict[str, Any]:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        async with httpx.AsyncClient() as client:
            response: httpx.Response = await client.post(self.token_url, data)
            response.raise_for_status()

            return ResponseHelper.process_incoming_network_response(
                response, TokenResponse
            )

    async def revoke_token(self, token: str) -> Any:
        if not hasattr(self, "revoke_token_url"):
            raise NotImplementedError(
                "Revoke token URL is not defined for this strategy."
            )

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.revoke_token_url,
                headers={"Authorization": f"Bearer {token}"},
            )
            response.raise_for_status()

            return ResponseHelper.process_incoming_network_response(response)

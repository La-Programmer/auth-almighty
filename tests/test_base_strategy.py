"""
Base strategy tests
"""

from typing import Optional
from urllib.parse import parse_qs, urlparse
from src.strategies.base_strategy import BaseStrategy


class TestBaseStrategy:
    def setup_method(self) -> None:
        """
        Setup class for handling base strategy testing
        """
        self.strategy = BaseStrategy(
            client_id="test-client-id",
            client_secret="test-client-secret",
            auth_url="test-auth-url",
            token_url="test-token-url",
            user_data_url="test-user-data-url",
            revoke_token_url="test-revoke-token-url",
        )

    def test_generate_url(self) -> None:
        scope = "openid email"
        redirect_uri = "test-redirect-uri"
        state = "tyrui924837tyrui"
        access_type = "offline"
        prompt = "consent"
        auth_url = self.strategy.generate_url(
            scope=scope,
            redirect_uri=redirect_uri,
            additional_parameters={
                "state": state,
                "access_type": access_type,
                "prompt": prompt,
            },
        )

        parsed_url = urlparse(auth_url)
        query_params = parse_qs(parsed_url.query)

        param_client_id: Optional[str] = query_params.get("client_id", [None])[0]
        param_redirect_uri: Optional[str] = query_params.get("redirect_uri", [None])[0]
        param_response_type: Optional[str] = query_params.get("response_type", [None])[
            0
        ]
        param_scope: Optional[str] = query_params.get("scope", [None])[0]
        param_state: Optional[str] = query_params.get("state", [None])[0]
        param_access_type: Optional[str] = query_params.get("access_type", [None])[0]
        param_prompt: Optional[str] = query_params.get("prompt", [None])[0]

        assert param_client_id == "test-client-id"
        assert param_redirect_uri == redirect_uri
        assert param_response_type == "code"
        assert param_scope == scope
        assert param_state == state
        assert param_access_type == access_type
        assert param_prompt == prompt

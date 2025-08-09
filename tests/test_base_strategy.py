"""
Base strategy tests
"""

from typing import Any, Optional
from unittest.mock import AsyncMock, MagicMock
from urllib.parse import parse_qs, urlparse

import httpx
import pytest
from pytest_mock import MockerFixture
from src.domain.enums.enums import GrantTypeEnum
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

    def _mock_successful_httpx_response(
        self, mocker: MockerFixture, response_data: dict[str, Any]
    ) -> AsyncMock:
        mock_response = MagicMock()
        mock_response.json.return_value = response_data
        mock_response.raise_for_status.return_value = None

        mock_post = AsyncMock(return_value=mock_response)

        mock_client = mocker.patch(
            "src.strategies.base_strategy.httpx.AsyncClient", autospec=True
        )
        mock_client.return_value.__aenter__.return_value.post = mock_post

        return mock_post

    def _mock_bad_request_httpx_response(
        self, mocker: MockerFixture, expected_exception: BaseException
    ) -> AsyncMock:
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = expected_exception

        mock_post = AsyncMock(return_value=mock_response)
        mock_client = mocker.patch(
            "src.strategies.base_strategy.httpx.AsyncClient", autospec=True
        )
        mock_client.return_value.__aenter__.return_value.post = mock_post

        return mock_post

    def _mock_invalid_json_response(
        self, mocker: MockerFixture, expected_exception: BaseException
    ) -> AsyncMock:
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = expected_exception

        mock_post = AsyncMock(return_value=mock_response)
        mock_client = mocker.patch(
            "src.strategies.base_strategy.httpx.AsyncClient", autospec=True
        )
        mock_client.return_value.__aenter__.return_value.post = mock_post

        return mock_post

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

    @pytest.mark.asyncio
    async def test_exchange_code_for_token(self, mocker: MockerFixture) -> None:
        expected_response = {
            "token_type": "Bearer",
            "access_token": "abc123",
            "refresh_token": "123abc",
        }

        mock_post = self._mock_successful_httpx_response(mocker, expected_response)

        code = "fake-code"

        result = await self.strategy.exchange_code_for_token(
            code, redirect_uri="https://redirect-uri"
        )

        assert result == expected_response

        mock_post.assert_called_once_with(
            "test-token-url",
            {
                "grant_type": GrantTypeEnum.AUTHORIZATION_CODE,
                "code": "fake-code",
                "redirect_uri": "https://redirect-uri",
                "client_id": "test-client-id",
                "client_secret": "test-client-secret",
            },
        )

    @pytest.mark.asyncio
    async def test_exchange_code_for_token_failure_case(
        self, mocker: MockerFixture
    ) -> None:
        expected_exception = httpx.HTTPStatusError(
            "Bad Request", request=MagicMock(), response=MagicMock(status_code=400)
        )

        self._mock_bad_request_httpx_response(mocker, expected_exception)

        code = "2443rrfrttg"
        redirect_uri = "test-redirect-uri"

        with pytest.raises(httpx.HTTPStatusError):
            await self.strategy.exchange_code_for_token(code, redirect_uri)

    @pytest.mark.asyncio
    async def test_exchange_code_for_invalid_json_case(
        self, mocker: MockerFixture
    ) -> None:
        expected_exception = RuntimeError("Response was not valid JSON.")

        self._mock_invalid_json_response(mocker, expected_exception)

        code = "2443rrfrttg"
        redirect_uri = "test-redirect-uri"

        with pytest.raises(RuntimeError):
            await self.strategy.exchange_code_for_token(code, redirect_uri)

    @pytest.mark.asyncio
    async def test_revoke_token(self, mocker: MockerFixture) -> None:
        token = "test-token"
        expected_response = {
            "status": "true",
            "message": "Token revoked successfully",
        }

        mock_post = self._mock_successful_httpx_response(mocker, expected_response)

        result = await self.strategy.revoke_token(token)
        assert result == expected_response

        mock_post.assert_called_once_with(
            "test-revoke-token-url",
            headers={"Authorization": f"Bearer {token}"},
        )

    @pytest.mark.asyncio
    async def test_revoke_token_bad_request(self, mocker: MockerFixture) -> None:
        token = "test-token"
        expected_exception = httpx.HTTPStatusError(
            "Bad Request", request=MagicMock(), response=MagicMock(status_code=400)
        )

        self._mock_bad_request_httpx_response(mocker, expected_exception)

        with pytest.raises(httpx.HTTPStatusError):
            await self.strategy.revoke_token(token)

    @pytest.mark.asyncio
    async def test_revoke_token_invalid_json(self, mocker: MockerFixture) -> None:
        token = "test_token"

        expected_exception = RuntimeError("Response was not valid JSON")

        self._mock_invalid_json_response(mocker, expected_exception)

        with pytest.raises(RuntimeError):
            await self.strategy.revoke_token(token)

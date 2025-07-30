import hashlib
import os
from urllib.parse import urlencode
import requests  # type: ignore

from src.strategies.base_strategy import BaseStrategy


# class GithubStrategy(BaseStrategy):
#     def __init__(
#         self,
#         client_id,
#         client_secret,
#         auth_url,
#         token_url,
#         user_data_url,
#         revoke_token_url,
#     ):
#         super().__init__(
#             client_id,
#             client_secret,
#             auth_url,
#             token_url,
#             user_data_url,
#             revoke_token_url,
#         )

#     def check_access_token(access_token):
#         with requests.post():
#             pass


# Generate url
# Handle code
# Exchange code for token
# Use token to make requests

import hashlib
import os
from urllib.parse import urlencode
import requests # type: ignore

GITHUB_CLIENT_ID = "Ov23licx3T2pngQBpQnJ"
GITHUB_CLIENT_SECRET = "f45d1964f6ddc01268e8e2c427128af8dce32b9b"
AUTH_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
SCOPE =[ 
    "repo"
    "repo:status"
    "repo_deployment"
    "public_repo"
    "public_repo"
    "repo:invite"
    "security_events"
    "notifications"
    "user"
    "read:user"
    "projects"
    "write:packages"
    "read:packages"
    "delete:packages"
]
REDIRECT_URL = "https://ideal-warm-boxer.ngrok-free.app/google/oauth"
HOST = "localhost"
PORT = 8080

def generate_url(params):
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "scope": SCOPE,
        "state": hashlib.sha256(os.urandom(1024)).hexdigest(),
        "redirect_url": REDIRECT_URL,
    }
    
    url = f"{AUTH_URL}?{urlencode(params)}"

def check_access_token(access_token):
    with requests.post():
        pass

# Generate url
# Handle code
    # Exchange code for token
    # Use token to make requests

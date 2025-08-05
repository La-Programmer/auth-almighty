from typing import List


class GrantTypeEnum:
    """
    Enum for different grant types used in OAuth2.
    """

    AUTHORIZATION_CODE: str = "authorization_code"
    IMPLICIT: str = "implicit"
    PASSWORD: str = "password"
    CLIENT_CREDENTIALS: str = "client_credentials"
    REFRESH_TOKEN: str = "refresh_token"

    @classmethod
    def choices(cls) -> List[str]:
        return [
            cls.AUTHORIZATION_CODE,
            cls.IMPLICIT,
            cls.PASSWORD,
            cls.CLIENT_CREDENTIALS,
            cls.REFRESH_TOKEN,
        ]

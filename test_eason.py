from typing import Dict
from audible.auth import Authenticator
import audible
import httpx

password ="Cc112211"
user="6061110@gmail.com"
myproxy="http://127.0.0.1:1080"
auth = Authenticator.from_login(
    username=user,
    proxys=myproxy,
    password=password,
    locale="us"
)
domain = "com"
cookies_domain = "com"


def refresh_website_cookies(
        refresh_token: str,
        domain: str,
        cookies_domain: str,
        with_username: bool = False
) -> Dict[str, str]:
    """Fetches website cookies for a specific domain.
    """

    target_domain = "audible" if with_username else "amazon"

    url = f"https://www.{target_domain}.{domain}/ap/exchangetoken/cookies"

    body = {
        "app_name": "Audible",
        "app_version": "3.56.2",
        "source_token": refresh_token,
        "requested_token_type": "auth_cookies",
        "source_token_type": "refresh_token",
        "domain": f".{target_domain}.{cookies_domain}"
    }

    resp = httpx.post(url, data=body)
    resp.raise_for_status()
    return resp.json()


new_cookies = refresh_website_cookies(
    refresh_token=auth.refresh_token,
    domain=domain,
    cookies_domain=cookies_domain
)
print(new_cookies)

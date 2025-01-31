"""
Implements base REST API.
"""

from typing import Optional, Union
import requests

DEFAULT_AUTH = 'rGTXZj6mQpsqwgEwQ4tYfQgn'


class BaseRest:
    """Base REST API."""

    def __init__(self, token: str = DEFAULT_AUTH) -> None:
        self.session = requests.Session()
        self.session.headers = {"Authorization": f"Bearer {token}"}
        self.session.verify = False
        self.base_url = "https://airportgap.com/api/"

    def get(self, url: str, params=None) -> Union[dict, list]:
        """Get rest command."""
        response = self.session.get(url, params=params)
        check_response(response)
        if response.text:
            return response.json()
        else:
            return {}

    def post(self, url: str, properties: dict) -> dict:
        """Post rest command."""
        response = self.session.post(url, json=properties)
        check_response(response)
        return response.json()

    def delete(self, url: str, params=None) -> dict:
        """Delete rest command."""
        response = self.session.delete(url, params=params)
        check_response(response)
        return response.json()

    def patch(self, url: str, json: Optional[dict] = None) -> dict:
        """Patch rest command."""
        response = self.session.patch(url, json=json)
        check_response(response)
        return response.json()

    def put(self, url: str, json: dict) -> dict:
        """Put rest command."""
        response = self.session.put(url, json=json)
        check_response(response)
        return response.json()


def check_response(response: requests.Response) -> None:
    """Check_response rest command."""
    # logger.debug(f"Response is {response}")
    if response.status_code >= 400:
        error_message = f"Error code is {response.status_code}, description {response.content.decode('utf-8').strip()}"
        #    logger.error(error_message)
        raise ValueError(error_message)
    if response.text:
        check_response_json(response, "Success")


def check_response_json(response: requests.Response, expect_message: str) -> None:
    """Check_response_json( rest command."""
    response_json = response.json()
    if "description" in response_json:
        description = response_json["description"]
        #  logger.debug(f"Response description is {description}")
        if expect_message not in description:
            #     logger.error(description)
            raise ValueError(description)

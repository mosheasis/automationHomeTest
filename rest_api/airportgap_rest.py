"""
Implements Airportgap REST API.
"""

from rest_api.base_rest import BaseRest


class AirportgapRest(BaseRest):

    def __init__(self) -> None:
        super().__init__()

    def generate_token(self, email: str, password: str) -> dict:
        """Generate a Token for the user."""
        add_user_url = self.base_url + "tokens"
        return self.post(add_user_url, properties={"email": email, "password": password})

    def get_airports(self):
        """
        Get list of all airports
        :return:
        """
        add_user_url = self.base_url + 'airports'
        airports = self.get(add_user_url)
        return airports

    def check_distance(self, airport_departure: str, airport_destination: str):
        """
        check distance for the airports

        :param airport_departure:
        :param airport_destination:
        :return:
        """
        add_user_url = self.base_url + "airports/distance"
        return self.post(add_user_url, properties={"from": airport_departure, "to": airport_destination})

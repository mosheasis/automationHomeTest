import pytest
from rest_api.airportgap_rest import *


@pytest.fixture(scope="function")
def airport_gap_rest():
    airport = AirportgapRest()
    return airport


@pytest.fixture(scope="function")
def gen_token(airport_gap_rest, email='moshe_asis@yahoo.com', password='airportgappassword'):
    token_new = airport_gap_rest.generate_token(email=email, password=password)
    return token_new['token']


@pytest.fixture(scope="function")
def get_airports(airport_gap_rest):
    airports = airport_gap_rest.get_airports()
    return airports


def test_get_airports(get_airports) -> None:
    """
    Scenario 1: Verify Airport Count"""
    assert len(get_airports['data']) == 30


def test_verify_airports(get_airports) -> None:
    """
    Scenario 2: Verify Specific Airports
    """

    airports_list = []
    for i in range(len(get_airports['data'])):
        airports_list.append(get_airports['data'][i]['attributes']['name'])
    assert 'Akureyri Airport' in airports_list
    assert 'St. Anthony Airport' in airports_list
    assert 'CFB Bagotville' in airports_list


def test_check_distance(airport_gap_rest) -> None:
    """
    Scenario 3:
        1. check distance for the airports KIX and NRT.
        2. Verify that the calculated distance between these airports is greater than 400 km.

    :param airport_gap_rest:
    :return:
    """
    result = airport_gap_rest.check_distance(from1="KIX", to="NRT")
    assert result['data']['attributes']['kilometers'] > 400

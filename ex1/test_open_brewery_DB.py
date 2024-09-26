import requests
import pytest

base_url = "https://api.openbrewerydb.org/breweries"


def test_get_breweries_by_city():
    city = "San Diego"
    response = requests.get(f"{base_url}?by_city={city}")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize("state", ["California", "Colorado"])
def test_get_breweries_by_state(state):
    response = requests.get(f"{base_url}?by_state={state}")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_single_brewery():
    brewery_id = "34e8c68b-6146-453f-a4b9-1f6cd99a5ada"
    response = requests.get(f"{base_url}/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id
    assert response.json()["country"] == "Lost Angeles"

def test_search_breweries():
    query = "dog"
    response = requests.get(f"{base_url}/search?query={query}")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize("brewery_id", ["34e8c68b-6146-453f-a4b9-1f6cd99a5ada", "9c5a66c8-cc13-416f-a5d9-0a769c87d318", "5128df48-79fc-4f0f-8b52-d06be54d0cec"])
def test_get_multiple_breweries(brewery_id):
    response = requests.get(f"{base_url}/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id


import pytest
from src.api import Api

@pytest.fixture(scope='function')
def breweries_api_user():
    return Api("https://api.openbrewerydb.org/v1/breweries")


@pytest.mark.parametrize("brewery_id", ["0759476d-8fed-46cc-abec-1cb02cbca0d6", "189df38b-d6a6-40c0-917e-5b172be8d859",
                                     "2907b143-57b4-49ec-aa41-07df64d1e14b"])
def test_breweries_existence(breweries_api_user, brewery_id):
    breweries_response = breweries_api_user.get_data(brewery_id, '')
    assert breweries_response.status_code == 200


def test_breweries_meta_data(breweries_api_user):
    expected_res = {
        "total": "8237",
        "page": "1",
        "per_page": "50"
    }
    breweries_response = breweries_api_user.get_data("meta", '').json()
    for key, value in expected_res.items():
        assert breweries_response[key] == value, (
            f'[{key}] Actual value: {breweries_response[key]}, expected: {value}'
        )


@pytest.mark.parametrize("country", ["united_states", "south_korea"])
def test_breweries_existence_by_country(breweries_api_user, country):
    breweries_response_by_country = breweries_api_user.get_data("?by_country="+country, None).json()
    breweries_response_by_country_metadata = breweries_api_user.get_data("meta?by_country="+country, None).json()
    assert breweries_response_by_country_metadata["total"] == str(len(breweries_response_by_country))


def test_get_random_breweries(breweries_api_user):
    random_breweries = breweries_api_user.get_data("random", None)
    assert random_breweries.status_code == 200


def test_list_get_random_breweries(breweries_api_user):
    list_breweries_response = breweries_api_user.get_data("?per_page=3", None)
    assert list_breweries_response.status_code == 200 and len(list_breweries_response.json()) == 3

import pytest
import requests


@pytest.mark.parametrize(
    ('brewery_id', 'status_code', 'brewery_data'),
    [
        pytest.param('5128df48-79fc-4f0f-8b52-d06be54d0cec', 200, {
            "id": "5128df48-79fc-4f0f-8b52-d06be54d0cec",
            "name": "(405) Brewing Co",
            "brewery_type": "micro",
            "address_1": "1716 Topeka St",
            "address_2": None,
            "address_3": None,
            "city": "Norman",
            "state_province": "Oklahoma",
            "postal_code": "73069-8224",
            "country": "United States",
            "longitude": -97.46818222,
            "latitude": 35.25738891,
            "phone": "4058160490",
            "website_url": "http://www.405brewing.com",
            "state": "Oklahoma",
            "street": "1716 Topeka St"
        }, id='first brewery'),
        pytest.param('1', 404, {}, id='not_found'),
    ]
)
def test_single_brewery(brewery_id, status_code, brewery_data):
    url = f"https://api.openbrewerydb.org/v1/breweries/{brewery_id}"

    response = requests.get(url)

    assert response.status_code == status_code
    if status_code == 200:
        response_json = response.json()
        for brewery_field, brewery_value in brewery_data.items():
            assert response_json.get(brewery_field) == brewery_value


@pytest.mark.parametrize(
    ('filter', 'status_code', 'count_breweries'),
    [
        pytest.param('', 200, 50, id='all breweries'),
        pytest.param('?by_city=Norman', 200, 3, id='by city Norman'),
        pytest.param('?by_country=United States', 200, 50, id='by country United States'),
        pytest.param('?by_name=(405) Brewing Co', 200, 1, id='by name (405) Brewing Co'),
        pytest.param('?by_city=awdawdawdawd', 200, 0, id='by city non exist'),
    ]
)
def test_list_breweries(filter, status_code, count_breweries):
    url = f"https://api.openbrewerydb.org/v1/breweries/{filter}"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == status_code
    assert len(response_json) == count_breweries


def test_random_brewery():
    url = "https://api.openbrewerydb.org/v1/breweries/random"

    response = requests.get(url)

    assert response.status_code == 200


def test_search_brewery():
    url = "https://api.openbrewerydb.org/v1/breweries/search?query=(405) Brewing Co"

    response = requests.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 14


def test_metadata():
    url = "https://api.openbrewerydb.org/v1/breweries/meta"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json.get('total') == 9527
    assert response_json.get('by_state').get('ACT') == 7

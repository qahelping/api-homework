import pytest
from jsonschema import validate

from schemas.schemas import brewery_schema


def test_get_brewery_list(brewery_api_client):
    response = brewery_api_client.get_breweries_list()
    assert response.ok
    instance = response.json()[0]
    assert instance
    validate(instance, brewery_schema)


@pytest.mark.parametrize(['bew_type', 'per_page'], [('micro', 2), ("regional", 3)])
def test_get_brewery_by_type(brewery_api_client, bew_type, per_page):
    response = brewery_api_client.get_breweries_by_type(bew_type, per_page)
    assert response.ok
    res = response.json()
    assert res
    assert len(res) <= per_page


@pytest.mark.parametrize(['bew_type', 'per_page'], [('test', 2), (0, 0)])
def test_get_brewery_by_type_negative(brewery_api_client, bew_type, per_page):
    response = brewery_api_client.get_breweries_by_type(bew_type, per_page)
    assert response.status_code == 400


def test_get_rand_brewery(brewery_api_client):
    response = brewery_api_client.get_rand_brewery(0)
    assert response.ok
    instance = response.json()[0]
    assert instance
    validate(instance, brewery_schema)


def test_get_rand_brewery_some(brewery_api_client):
    response = brewery_api_client.get_rand_brewery(3)
    assert response.ok
    assert len(response.json()) == 3


def test_get_rand_brewery_negative(brewery_api_client):
    response = brewery_api_client.get_rand_brewery(-8)
    assert response.status_code == 500

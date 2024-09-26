import pytest
from requests import Response
from pytest_voluptuous import S
from ex2.ddt_api_testing.shemas import shemas_brewery
import uuid
import logging


def test_get_single_brewery(brewery_api):
    # GIVEN:
    obdb_id = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"

    # WHEN:
    response: Response = brewery_api.get(
        url=f"/{obdb_id}",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json() == S(shemas_brewery.get_single_brewery)
    # logging.info(response.json())


@pytest.mark.parametrize("pages_num", [3, 5, 7, 8, 10])
def test_get_list_breweries(brewery_api, pages_num):
    # GIVEN:

    # WHEN:
    response: Response = brewery_api.get(
        url=f"?per_page={pages_num}",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())


@pytest.mark.parametrize(
    "city, page_num",
    [
        ("san_diego", 3),
    ],
)
def test_get_breweries_by_city(brewery_api, city, page_num):
    # GIVEN:

    # WHEN:
    response: Response = brewery_api.get(
        url=f"?by_city={city}&per_page={page_num}",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())


@pytest.mark.parametrize(
    "btype, page_num",
    [
        ("micro", 3),
        ("regional", 8),
        ("contract", 5),
        ("large", 2),
        ("brewpub", 7),
    ],
)
def test_get_breweries_by_type(brewery_api, btype, page_num):
    # GIVEN:

    # WHEN:
    response: Response = brewery_api.get(
        url=f"?by_type={btype}&per_page={page_num}",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())


def test_get_breweries_meta(brewery_api):
    # GIVEN:

    # WHEN:
    response: Response = brewery_api.get(
        url="/meta",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())

import pytest
from requests import Response
from pytest_voluptuous import S
from ex2.ddt_api_testing.shemas import shemas_dogapi
import logging


def test_get_list_all_breeds(dog_api):
    # GIVEN:

    # WHEN:
    response: Response = dog_api[0].get(
        url="/list/all",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json() == S(shemas_dogapi.get_list_dogs)
    # logging.info(response.json())


def test_get_list_all_sub_breeds(dog_api):
    # GIVEN:

    # WHEN:
    response: Response = dog_api[1].get(
        url="/hound/list",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json() == S(shemas_dogapi.list_all_sub_breeds)
    # logging.info(response.json())


def test_get_all_images(dog_api):
    # GIVEN:

    # WHEN:
    response: Response = dog_api[1].get(
        url="/hound/images",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())


@pytest.mark.parametrize(
    "names",
    [
        "affenpinscher",
        "african",
        "airedale",
        "akita",
        "appenzeller",
        "basenji",
        "chihuahua",
    ],
)
def test_get_images_by_breed(dog_api, names):
    # GIVEN:

    # WHEN:

    response: Response = dog_api[1].get(
        url=f"/{names}/images/random",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())


@pytest.mark.parametrize(
    "number_images",
    [1, 2, 3, 4, 50, 100500],
)
def test_get_images_by_breed(dog_api, number_images):
    # GIVEN:

    # WHEN:

    response: Response = dog_api[0].get(
        url=f"/image/random/{number_images}",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"
    # logging.info(response.json())

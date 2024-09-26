import pytest
from requests import Response
from pytest_voluptuous import S
from ex2.ddt_api_testing.shemas import shemas_jsonplaceholder
from mimesis.enums import Locale
from mimesis import Person
import random
import logging


def test_get_placeholders(jsonplaceholder_api):
    # GIVEN:

    # WHEN:
    response: Response = jsonplaceholder_api.get(
        url="/posts",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    # assert response.json() == S(shemas_jsonplaceholder.create_user)
    # # logging.info(response.json())


def test_get_placeholder_num(jsonplaceholder_api):
    # GIVEN:

    # WHEN:
    response: Response = jsonplaceholder_api.get(
        url="/posts/1",
        # data=user_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.json() == S(shemas_jsonplaceholder.create_user)
    # # logging.info(response.json())


@pytest.mark.parametrize("userIds", [1, 2, 3, 4, 5], ids=[1, 2, 3, 4, 5])
def test_post_placeholder(jsonplaceholder_api, userIds):
    # GIVEN:
    placeholder = Person(Locale.EN)
    placeholder_data = {
        "userId": userIds,
        "id": random.randint(1, 10),
        "title": placeholder.title(),
        "body": placeholder.full_name(),
    }

    # WHEN:
    response: Response = jsonplaceholder_api.post(url="/posts", data=placeholder_data)

    # THEN:
    assert response.status_code == 201
    assert response.reason == "Created"


def test_patch_placeholder(jsonplaceholder_api):
    # GIVEN:
    placeholder = Person(Locale.EN)
    placeholder_data = {
        "userId": 1,
        "id": 1,
        "title": placeholder.title(),
        "body": placeholder.full_name(),
    }

    # WHEN:
    response: Response = jsonplaceholder_api.patch(
        url="/posts/1", data=placeholder_data
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"


@pytest.mark.parametrize("userIds", [1, 2, 3, 4, 5], ids=[1, 2, 3, 4, 5])
def test_delete_placeholder(jsonplaceholder_api, userIds):
    # GIVEN:

    # WHEN:
    response: Response = jsonplaceholder_api.delete(
        url=f"/posts/{userIds}",
    )

    # THEN:
    assert response.status_code == 200
    assert response.reason == "OK"

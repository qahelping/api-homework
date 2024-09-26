import requests
import pytest


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("url")


@pytest.fixture(scope="session")
def status_code(request):
    return request.config.getoption("status_code")


def test_get_post_by_id_with_param(url, status_code):
    response = requests.get(url + "/posts/1", params={"param": "value"})
    assert response.status_code == status_code
    assert response.json()["id"] == 1
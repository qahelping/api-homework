import pytest

from dogs_api_client.dogs_api_client import DogsApiClient
from helpers.dogs_api_helper import DogsApiHelper

from brevery_api_client.brevery_api_client import BreweryApiClient

from JSONPlaceholder.placeholder_api_client import PlaceholderApiClient


@pytest.fixture(scope="session")
def dogs_api_client():
    client = DogsApiClient()
    return client


@pytest.fixture(scope="function")
def dogs_api_helper(dogs_api_client):
    helper = DogsApiHelper(dogs_api_client)
    return helper


@pytest.fixture(scope="function")
def brewery_api_client():
    client = BreweryApiClient()
    return client


@pytest.fixture(scope="function")
def placeholder_api_client():
    client = PlaceholderApiClient()
    return client


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status",
        default=200,
        choices=["200", "404", "500"],
        help="Status code expected to get",
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status")
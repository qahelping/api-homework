from datetime import datetime
import pytest
from gectaro_http_client import GectaroHttpClient
from models import PostResourceRequests, PostProjectTaskResource


def pytest_addoption(parser):
    parser.addoption("--token", help="token for test API")
    parser.addoption(
        "--url", default="https://api.gectaro.com", help="base url for API client"
    )


@pytest.fixture(scope="session")
def token(request):
    return request.config.getoption("--token")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def client(token, url):
    client = GectaroHttpClient(base_url=url, token=token)
    yield client
    # teardown


@pytest.fixture
def resource(client):
    json_data_for_resource = PostProjectTaskResource(
        **{
            "name": "first_resource",
            "needed_at": int(datetime.now().timestamp()),
            "project_id": client.project_id,
            "type": 2,
            "volume": 5,
        }
    )

    response = client.post_projects_resources(json_data=json_data_for_resource)
    resource_id = response.json()["id"]

    yield resource_id


#     если бы в сваггере был описан метод удаления ресурса, я бы его обязательно удалил

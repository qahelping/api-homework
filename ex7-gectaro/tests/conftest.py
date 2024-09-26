from datetime import datetime

import pytest

from tests.gectaro_http_client import GectaroHttpClient
from tests.response_models import ResourceRequest


def pytest_addoption(parser):
    parser.addoption("--token", help="token for test API")
    parser.addoption("--url", default="https://api.gectaro.com",
                     help="url for test API")


@pytest.fixture(scope='session')
def token(request):
    return request.config.getoption('--token')


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def client(token, base_url):
    client = GectaroHttpClient(base_url=base_url,
                               token=token)
    yield client


@pytest.fixture()
def resource(client):
    data = {
        "name": "Resource Name",
        "needed_at": int(datetime.now().timestamp()),
        "project_id": client.project_id,
        "type": 1,
        "volume": 44.0
    }
    resource_response = client.post_projects_resource(data)
    assert resource_response.status_code == 201
    resource_id = resource_response.json()['id']
    yield resource_id
    resource_delete_response = client.delete_projects_resource(resource_id)
    assert resource_delete_response.status_code == 204, f"Resource {resource_id} doesnt deleted"


@pytest.fixture()
def resource_request_id(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    yield response.json()[0]['id']


@pytest.fixture()
def resource_request(resource, client):
    data = {"project_tasks_resource_id": resource,
            "volume": 44.0,
            "cost": 55.0,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 201
    ResourceRequest(**response.json())
    new_resource_request_id = response.json()['id']
    yield new_resource_request_id



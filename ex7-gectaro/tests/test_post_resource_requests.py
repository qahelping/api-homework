from datetime import datetime

import pytest

from tests.response_models import ResourceRequest


def test_post_resource_request_success(client, resource):
    data = {"project_tasks_resource_id": resource,
            "volume": 44.0,
            "cost": 55.0,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 201
    ResourceRequest(**response.json())


def test_post_resource_request_is_over_budget_false(client, resource):
    data = {"project_tasks_resource_id": resource,
            "volume": 44.0,
            "cost": 55.0,
            "is_over_budget": False,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422


def test_post_resource_request_missing_required_field(client, resource):
    data = {"volume": 44.0,
            "cost": 55.0,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422


def test_post_resource_request_invalid_resource_id(client, resource):
    data = {"project_tasks_resource_id": 0,
            "volume": 44.0,
            "cost": 55.0,
            "is_over_budget": False,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 422


@pytest.mark.parametrize("volume,cost,expected_status", [
    (44.0, 55.0, 201),
    (1.0, 0, 201),
    (-1, 55.0, 422),
    (44.0, -1, 422)],
                         ids=[
                             "positive case with normal values",
                             "positive case with minimal values",
                             "negative case with volume=-1",
                             "negative case with cost=-1"])
def test_post_resource_request_volume_and_cost(client, resource, volume, cost, expected_status):
    data = {"project_tasks_resource_id": resource,
            "volume": volume,
            "cost": cost,
            "is_over_budget": True,
            "needed_at": int(datetime.now().timestamp())}
    response = client.post_projects_resource_request(data=data)
    assert response.status_code == expected_status

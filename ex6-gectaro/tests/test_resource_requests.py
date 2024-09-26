from gectaro_http_client import GectaroHttpClient
from datetime import datetime
from models import GetResourceRequests, GetResourceRequestsId, GetCompanies
import pytest
import requests


###################################################################
#                 GET v1/projects/id/resource-requests            #
###################################################################
def test_get_resource_requests(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    GetResourceRequests(project_tasks=response.json())


def test_403_get_resource_requests(client):
    """передан id проекта, к которому запрещен доступ"""
    response = client.session.get(
        f"{client.base_url}/v1/projects/11111/resource-requests"
    )
    assert response.status_code == 403


###################################################################
#                GET v1/projects/id/resource-requests/id          #
###################################################################
def test_get_resource_requests_request_id(client):
    req_id = client.get_projects_resource_requests().json()[0]["id"]
    response = client.get_projects_resource_requests_id(request_id=req_id)
    assert response.status_code == 200
    GetResourceRequestsId(**response.json())


def test_404_get_resource_requests_request_id(client):
    """передан несуществующий request_id"""
    response = client.get_projects_resource_requests_id(request_id=1111111)
    assert response.status_code == 404


###################################################################
#                 POST v1/projects/id/resource-requests           #
###################################################################
@pytest.mark.parametrize("volume", (1, 1000), ids=("volume=1", "volume=1000"))
@pytest.mark.parametrize("cost", (1, 1000), ids=("cost=1", "cost=1000"))
def test_post_resource_requests(client, resource, cost, volume):
    json_data = {
        "project_tasks_resource_id": resource,
        "volume": volume,
        "cost": cost,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": 1,
    }

    response = client.post_projects_resource_requests(data=json_data)
    assert response.status_code == 201


def test_422_post_resource_requests(client, resource):
    """передан параметр is_over_budjet=False"""

    json_data = {
        "project_tasks_resource_id": resource,
        "volume": 5,
        "cost": 44,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": 0,
    }

    response = client.post_projects_resource_requests(data=json_data)
    assert response.status_code == 422


###################################################################
#                 PUT v1/projects/id/resource-requests            #
###################################################################
def test_put_resource_requests(client, resource):
    json_data = {
        "project_tasks_resource_id": resource,
        "volume": 5,
        "cost": 8,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": 1,
    }

    req_id = client.post_projects_resource_requests(data=json_data).json()["id"]
    new_volume = 18
    json_data["volume"] = new_volume

    response = client.put_projects_resource_requests(request_id=req_id, data=json_data)
    assert response.status_code == 200

    response_get = client.get_projects_resource_requests_id(request_id=req_id)
    assert int(float(response_get.json()["volume"])) == new_volume


def test_422_put_resource_requests(client, resource):
    """не передан project_tasks_resource_id"""
    json_data = {
        "project_tasks_resource_id": resource,
        "volume": 5,
        "cost": 8,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": 1,
    }

    req_id = client.post_projects_resource_requests(data=json_data).json()["id"]
    json_data["project_tasks_resource_id"] = None

    response = client.put_projects_resource_requests(request_id=req_id, data=json_data)
    assert response.status_code == 422


###################################################################
#                DELETE v1/projects/id/resource-requests          #
###################################################################
def test_delete_resource_requests(client, resource):
    json_data = {
        "project_tasks_resource_id": resource,
        "volume": 5,
        "cost": 8,
        "needed_at": int(datetime.now().timestamp()),
        "is_over_budget": 1,
    }

    req_id = client.post_projects_resource_requests(data=json_data).json()["id"]

    response = client.delete_projects_resource_requests(request_id=req_id)
    assert response.status_code == 204

    response_get = client.get_projects_resource_requests_id(request_id=req_id)
    assert response_get.status_code == 404


def test_404_delete_resource_requests(client):
    """передан несуществующий request_id"""
    response = client.delete_projects_resource_requests(request_id=1111111)
    assert response.status_code == 404


###################################################################
#                          GET v1/companies                       #
###################################################################
def test_get_companies(client):
    response = client.get_companies()
    assert response.status_code == 200
    GetCompanies(companies=response.json())


def test_401_get_companies(client):
    """запрос без авторизации"""
    response = requests.get("https://api.gectaro.com/v1/companies")
    assert response.status_code == 401


###################################################################
#                GET v1/companies/id/resource-requests            #
###################################################################
def test_get_company_resource_requests(client):
    company_id = client.get_companies().json()[0]["id"]
    response = client.get_company_resource_requests(company_id=company_id)
    assert response.status_code == 200
    GetResourceRequests(project_tasks=response.json())


def test_404_get_company_resource_requests(client):
    """передан несуществующий company_id"""
    response = client.get_company_resource_requests(company_id=1111111)
    assert response.status_code == 404

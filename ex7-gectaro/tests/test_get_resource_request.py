from tests.response_models import ResourceRequestResponse, ResourceRequest


def test_get_resource_request(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    ResourceRequestResponse(project_tasks=response.json())


def test_get_resource_request_invalid_project_id(client):
    client.set_project_id(0)
    response = client.get_projects_resource_requests()
    assert response.status_code == 404


def test_get_resource_request_len_id(client):
    response = client.get_projects_resource_requests()
    assert response.status_code == 200
    ResourceRequestResponse(project_tasks=response.json())
    for item in response.json():
        assert len(str(item['id'])) >= 7


def test_get_resource_request_by_id(client, resource_request_id):
    response = client.get_projects_resource_request_by_id(resource_request_id)
    assert response.status_code == 200
    ResourceRequest(**response.json())


def test_get_resource_request_by_invalid_id(client):
    response = client.get_projects_resource_request_by_id(6)
    assert response.status_code == 404


def test_get_resource_request_by_company_id(client):
    response = client.get_companies_resource_request()
    assert response.status_code == 200
    ResourceRequestResponse(project_tasks=response.json())

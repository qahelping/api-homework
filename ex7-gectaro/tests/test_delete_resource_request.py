from datetime import datetime

import pytest


def test_delete_resource_request_success(client, resource):
    data = {
        "project_tasks_resource_id": resource,
        "volume": 50.0,
        "cost": 100.0,
        "is_over_budget": True,
        "needed_at": int(datetime.now().timestamp())
    }
    response = client.post_projects_resource_request(data)
    assert response.status_code == 201
    new_resource_request_id = response.json()['id']
    response_delete = client.delete_projects_resource_request(new_resource_request_id)
    assert response_delete.status_code == 204


def test_delete_resource_request_over_budget_false(client, resource):
    data = {
        "project_tasks_resource_id": resource,
        "volume": 50.0,
        "cost": 100.0,
        "is_over_budget": False,
        "needed_at": int(datetime.now().timestamp())
    }
    response = client.post_projects_resource_request(data)
    assert response.status_code == 201
    new_resource_request_id = response.json()['id']
    response_delete = client.delete_projects_resource_request(new_resource_request_id)
    assert response_delete.status_code == 422
    assert response_delete.json()['message'] == 'Запрещено удалять заявки на заказы сверх бюджета.'


@pytest.mark.parametrize("order_status, status_code",
                         [(10, 400), (20, 400)],
                         ids=["draft", "waiting for payment"])
def test_put_resource_request_included_in_order_in_status_draft(client, resource_request, order_status, status_code):
    contractor_id = client.get_companies_contractors().json()[0]['id']
    stock_id = client.get_companies_stocks().json()[0]['id']
    data_orders = {
        "contractor_id": contractor_id,
        "pay_until_date": int(datetime.now().timestamp() + 3600),
        "status": order_status,
        "items": [{
            "resource_request_id": resource_request,
            "volume": 100,
            "cost": 500
        }],
        "stock_id": stock_id
    }
    client.post_projects_orders(data_orders)

    response = client.delete_projects_resource_request(resource_request_id=resource_request)
    assert response.status_code == status_code, (f"Expected {status_code}, got {response.status_code} with response"
                                                 f" {response.content}")


def test_delete_nonexistent_resource_request(client):
    response = client.delete_projects_resource_request(999999999)
    assert response.status_code == 404
    assert response.json()['message'] == "not_found_project_task_resource"

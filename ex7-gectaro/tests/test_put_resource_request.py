from datetime import datetime

import pytest

from tests.response_models import ResourceRequest


@pytest.mark.parametrize("cost, volume", [(100, 50)], ids=["cost: 100, volume:50"])
def test_put_resource_request_change_cost_and_volume(client, resource_request, cost, volume):
    data = {"volume": volume,
            "cost": cost}
    response = client.put_projects_resource_request(resource_request_id=resource_request, data=data)
    assert response.status_code == 200
    ResourceRequest(**response.json())
    assert response.json()['cost'] == cost
    assert response.json()['volume'] == volume


def test_put_resource_request_change_needed_at(client, resource_request):
    data = {
        "needed_at": int(datetime.now().timestamp() + 3600)
    }
    response = client.put_projects_resource_request(resource_request_id=resource_request, data=data)
    assert response.status_code == 200
    ResourceRequest(**response.json())


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
    created_order_id = client.post_projects_orders(data_orders).json()['id']

    data = {
        "needed_at": int(datetime.now().timestamp() + 3600)
    }
    response = client.put_projects_resource_request(resource_request_id=resource_request, data=data)
    deleted_order = client.delete_companies_orders(created_order_id)
    assert deleted_order.status_code == 204
    assert response.status_code == status_code, (f"Expected {status_code}, got {response.status_code} with response"
                                                 f" {response.content}")


def test_put_resource_request_not_over_budget(client, resource):
    data = {
        "project_tasks_resource_id": resource,
        "volume": 50.0,
        "cost": 100.0,
        "is_over_budget": False,
        "needed_at": int(datetime.now().timestamp())
    }

    response = client.post_projects_resource_request(data=data)
    assert response.status_code == 201
    data = {
        "cost": 100.0,
        "is_over_budget": True,
    }
    new_resource_request_id = response.json()['id']
    response_put = client.put_projects_resource_request(data=data, resource_request_id=new_resource_request_id)
    assert response_put.status_code == 400

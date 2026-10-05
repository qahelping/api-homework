import pytest
import requests


@pytest.mark.parametrize(
    ('resource_id', 'status_code', 'resource_data'),
    [
        pytest.param(1, 200, {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }, id='first resource'),
        pytest.param(98712639871264876128746128424, 404, {}, id='not_found'),
    ]
)
def test_getting_a_resource(resource_id, status_code, resource_data):
    url = f"https://jsonplaceholder.typicode.com/posts/{resource_id}"

    response = requests.get(url)

    assert response.status_code == status_code

    response_json = response.json()
    for brewery_field, brewery_value in resource_data.items():
        assert response_json.get(brewery_field) == brewery_value


def test_listing_all_resources():
    url = f"https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json) == 100


@pytest.mark.parametrize(
    ('resource_id', 'status_code', 'resources_count'),
    [
        pytest.param(1, 200, 10, id='first resource'),
        pytest.param(98712639871264876128746128424, 200, 0, id='not_found'),
    ]
)
def test_filtering_resources(resource_id, status_code, resources_count):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={resource_id}"

    response = requests.get(url)

    assert response.status_code == status_code
    assert len(response.json()) == resources_count


@pytest.mark.parametrize(
    ('resource_id', 'status_code', 'resources_count'),
    [
        pytest.param(1, 200, 5, id='first resource'),
        pytest.param(98712639871264876128746128424, 200, 0, id='not_found'),
    ]
)
def test_listing_nested_resources(resource_id, status_code, resources_count):
    url = f"https://jsonplaceholder.typicode.com/posts/{resource_id}/comments"

    response = requests.get(url)

    assert response.status_code == status_code
    assert len(response.json()) == resources_count


@pytest.mark.parametrize(
    ('resource_id', 'status_code'),
    [
        pytest.param(1, 200, id='first resource'),
        pytest.param(98712639871264876128746128424, 200, id='not_found'),
    ]
)
def test_deleting_a_resource(resource_id, status_code):
    url = f"https://jsonplaceholder.typicode.com/posts/{resource_id}"

    response = requests.delete(url)

    assert response.status_code == status_code

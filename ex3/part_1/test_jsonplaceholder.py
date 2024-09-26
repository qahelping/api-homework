import pytest
from src.api import Api


@pytest.fixture(scope='function')
def json_api():
    return Api("https://jsonplaceholder.typicode.com")


@pytest.mark.parametrize("id_num", ["1", "10", "20"])
def test_get_posts(json_api, id_num):
    response = json_api.get_data("posts", id_num).json()
    assert str(response["id"]) == id_num


@pytest.mark.parametrize("id_num", ["1", "10", "20"])
def test_get_comments(json_api, id_num):
    response = json_api.get_data("comments?postId="+id_num, None).json()
    for count in range(0, len(response)):
        assert str(response[count]["postId"]) == id_num

@pytest.mark.parametrize("id_num, data",
                         [("1", {
                                  "userId": 1,
                                  "id": 1,
                                  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                                  "body": "somebody_1"
                                }),
                          ("10", {
                                  "userId": 1,
                                  "id": 10,
                                  "title": "optio molestias id quia eum",
                                  "body": "somebody_2"
                                }),
                          ("20", {
                                  "userId": 2,
                                  "id": 20,
                                  "title": "doloribus ad provident suscipit at",
                                  "body": "somebody_3"
                                })
                           ])
def test_put_posts(json_api, id_num, data):
    data_id = json_api.put_data("posts",id_num, data)
    assert data_id
    response = json_api.get_data("posts", id_num).json()
    for key, value in data.items():
        assert response[key] == value, (
            f'[{key}] Actual value: {response[key]}, expected: {value}'
        )


@pytest.mark.parametrize("id_num, key_value",
                         [("1", {"userId": 10, "body": "somebody_1"}),
                          ("10", {"userId": 20, "body": "somebody_2"}),
                          ("20", {"userId": 30, "body": "somebody_3"})
                          ])
def test_patch_posts(json_api, id_num, key_value):
    data_id = json_api.patch_data("posts", id_num, key_value)
    assert data_id
    response = json_api.get_data("posts", id_num).json()
    for key, value in key_value.items():
        assert response[key] == value, (
            f'[{key}] Actual value: {response[key]}, expected: {value}'
        )


@pytest.mark.xfail()
@pytest.mark.parametrize("id_num", ["1", "10", "20"])
def test_delete_data(json_api, id_num):
    json_api.delete_data("posts", id_num)
    response = json_api.get_data("posts", id_num).json()
    assert response
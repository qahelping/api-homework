import requests

JSON_URL = "https://jsonplaceholder.typicode.com/posts"


def test_get_posts():
    response = requests.get(JSON_URL)
    assert response.status_code == 200

    res = response.json()[0]
    assert res[0]["id"] > 0
    assert response.json()[0]["userId"] > 0
    assert response.json()[0]["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert response.json()[0][
               "body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"


def test_get_post_by_id():
    response = requests.get(f"{JSON_URL}/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_post_by_id_with_param():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", params={"param": "value"})
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_post_by_id_with_param_and_param():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", params={"param": "value", "page": 2})
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_post_by_id_with_param_and_param_and_param():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1",
                            params={"param": "value", "page": 2, "limit": 10})
    assert response.status_code == 200
    assert response.json()["id"] == 1

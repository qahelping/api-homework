import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


@pytest.mark.parametrize("post_id", [1, 3, 7])
def test_get_comments_by_post_id(post_id):
    response = requests.get(f"{BASE_URL}/comments", params={"postId": post_id})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for comment in data:
        assert comment["postId"] == post_id


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user_id(user_id):
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for post in data:
        assert post["userId"] == user_id


def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    user = data[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user
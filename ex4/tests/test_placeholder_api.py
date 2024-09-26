import pytest
from models import placeholder_model


def test_get_posts(placeholder_api_client):
    response = placeholder_api_client.get_posts()
    assert response.ok

    res = response.json()
    posts = [placeholder_model.Posts.model_validate(obj) for obj in res]
    for post in posts:
        assert post.userId > 0
        assert post.id > 0
        assert post.title


def test_get_users(placeholder_api_client):
    response = placeholder_api_client.get_users()
    assert response.ok

    res = response.json()
    users = [placeholder_model.User.model_validate(obj) for obj in res]
    for user in users:
        assert user.id > 0
        assert user.username


@pytest.mark.parametrize(["user_id", "amount"],
                         [(0, 200), (1, 20), (-1, 0), (11, 0), ("abc", 0)])
def test_get_todos(placeholder_api_client, user_id, amount):
    response = placeholder_api_client.get_todos(user_id)
    assert response.ok

    ret_amount = len(response.json())
    assert ret_amount == amount

    if ret_amount:
        todos = [placeholder_model.Todos.model_validate(obj) for obj in response.json()]
        for todo in todos:
            assert todo.userId == user_id or user_id == 0


def test_get_comments(placeholder_api_client):
    response = placeholder_api_client.get_post_comments(3)
    assert response.ok


@pytest.mark.parametrize(["album_id", "status_code"], [(1, 200), (101, 404),  (-5, 404), ("abc", 404)])
def test_get_album(placeholder_api_client, album_id, status_code):
    response = placeholder_api_client.get_album(album_id)
    assert response.status_code == status_code


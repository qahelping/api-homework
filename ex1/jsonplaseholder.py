import pytest
import requests


def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert response.json()[0]["id"] > 0


def test_get_post_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
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
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", params={"param": "value", "page": 2, "limit": 10})
    assert response.status_code == 200
    assert response.json()["id"] == 1
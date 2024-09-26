import pytest
import requests


def test_get_breed_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_get_breed_info():
    response = requests.get("https://dog.ceo/api/breed/husky/images")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_get_breed_list_with_param():
    response = requests.get("https://dog.ceo/api/breeds/list/random")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_get_breed_info_with_param():
    response = requests.get("https://dog.ceo/api/breed/bulldog/images")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_get_breed_info_with_param_and_param():
    response = requests.get("https://dog.ceo/api/breed/bulldog/images", params={"limit": 2})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
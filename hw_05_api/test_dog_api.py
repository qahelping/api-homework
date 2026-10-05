from enum import Enum

import pytest
import requests

BASE_URL = "https://dog.ceo/api"


def test_list_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], dict)
    assert len(data["message"]) > 0


def test_random_image():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    assert 'message' in response.text
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert isinstance(data["message"], str)


@pytest.mark.parametrize("count", [1, 2, 3])
def test_random_multiple_images(count):
    response = requests.get(f"{BASE_URL}/breeds/image/random/{count}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) == count


@pytest.mark.parametrize("breed", ["akita", "coonhound", "doberman"])
def test_random_image_by_breed(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], str)
    assert breed in data["message"]


@pytest.mark.parametrize("breed", ["bulldog",  "retriever", "hound"])
def test_sub_breed_list(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/list")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) > 0




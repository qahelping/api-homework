#python -m pytest tests_api -v
import pytest
import requests


def test_list_all():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200, "Status code is not 200"
    json_result = response.json()
    assert json_result["status"] == "success", "Status is not success"
    assert isinstance(json_result["message"], dict)
    assert len(json_result["message"]) > 0

def test_random():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200, "Status code is not 200"
    json_result = response.json()
    assert json_result["status"] == "success", "Status is not success"
    assert isinstance(json_result["message"], str)
    assert json_result["message"].startswith("https://images.dog.ceo/breeds")
    assert json_result["message"].endswith(".jpg")

@pytest.mark.parametrize("breed", ["akita", "samoyed", "ovcharka"])
def test_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200, "Status code is not 200"
    json_result = response.json()
    assert json_result["status"] == "success", "Status is not success"
    assert isinstance(json_result["message"], str), "Message is not string"
    assert json_result["message"].startswith(f"https://images.dog.ceo/breeds/{breed}")

@pytest.mark.parametrize("amount", [1, 19, 50])
def test_by_amount(amount):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{amount}")
    assert response.status_code == 200, "Status code is not 200"
    json_result = response.json()
    assert json_result["status"] == "success", "Status is not success"
    assert isinstance(json_result["message"], list)
    assert len(json_result["message"]) == amount
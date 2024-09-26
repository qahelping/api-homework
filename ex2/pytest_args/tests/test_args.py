import requests
from requests import Response


def test_addition(url, status_code):
    response: Response = requests.get(url)
    assert response.status_code == status_code

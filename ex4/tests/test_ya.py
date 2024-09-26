import requests


def test_address(status_code, base_url):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url=base_url, headers=headers)
    assert response.status_code == int(status_code)

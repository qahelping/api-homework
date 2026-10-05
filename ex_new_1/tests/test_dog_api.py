import pytest
import requests


def test_list_all_breeds():
    url = "https://dog.ceo/api/breeds/list/all"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json.get('message')
    assert response_json.get('status') == 'success'


def test_random_image():
    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json.get('message')
    assert response_json.get('status') == 'success'


@pytest.mark.parametrize(
    ('breed', 'status_code', 'status'),
    [
        pytest.param('akita', 200, 'success', id='akita'),
        pytest.param('al;wjdlkjalwkf', 404, 'error', id='not_found'),
    ]
)
def test_by_breed(breed, status_code, status):
    url = f"https://dog.ceo/api/breed/{breed}/images"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == status_code
    assert response_json.get('message')
    if status_code == 200:
        assert isinstance(response_json.get('message'), list)
    else:
        assert isinstance(response_json.get('message'), str)
    assert response_json.get('status') == status


@pytest.mark.parametrize(
    ('breed', 'status_code', 'status'),
    [
        pytest.param('hound', 200, 'success', id='hound'),
        pytest.param('al;wjdlkjalwkf', 404, 'error', id='not_found'),
    ]
)
def test_by_sub_breed(breed, status_code, status):
    url = f"https://dog.ceo/api/breed/{breed}/list"

    response = requests.get(url)
    response_json = response.json()

    assert response.status_code == status_code
    assert response_json.get('message')
    if status_code == 200:
        assert isinstance(response_json.get('message'), list)
    else:
        assert isinstance(response_json.get('message'), str)
    assert response_json.get('status') == status


@pytest.mark.parametrize(
    ('breed', 'status_code', 'status'),
    [
        pytest.param('akita', 200, 'success', id='akita'),
        pytest.param('al;wjdlkjalwkf', 404, 'error', id='not_found'),
    ]
)
def test_browse_breed_list(breed, status_code, status):
    url = f"https://dog.ceo/api/breed/{breed}/images/random/"

    response = requests.get(url)

    response_json = response.json()

    assert response.status_code == status_code
    assert response_json.get('message')
    assert isinstance(response_json.get('message'), str)
    assert response_json.get('status') == status

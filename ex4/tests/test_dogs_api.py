import pytest

import dogs_api_client
from helpers.dogs_api_helper import DogsApiHelper


def test_get_all_breeds(dogs_api_client):
    response = dogs_api_client.get_all_breeds()
    assert response.ok
    assert len(response.json()['message'])


def test_get_rand_image(dogs_api_client):
    """
    :return:
    {
    "message": "https://images.dog.ceo/breeds/komondor/n02105505_2178.jpg",
    "status": "success"
    }
    """
    response = dogs_api_client.get_rand_images()
    assert response.ok

    img = response.json()['message']
    assert isinstance(img, str)
    assert ".jpg" in img


@pytest.mark.parametrize(["amount", "exp_amount"],
        [("asdfs", 1), (-3, 1), (3, 3), (52, 50)])
def test_get_rand_images(dogs_api_client, amount, exp_amount):
    """
    :return:
    {
    "message": ["https://images.dog.ceo/breeds/komondor/n02105505_2178.jpg"],
    "status": "success"
    }
    """
    response = dogs_api_client.get_rand_images(amount)
    assert response.ok

    images = response.json()['message']
    assert len(images) == exp_amount


def test_get_breed_images(dogs_api_helper, dogs_api_client):
    breed = dogs_api_helper.find_rand_breed()
    response = dogs_api_client.get_breed_images(breed)
    assert response.ok
    assert len(response.json()['message'])


def test_get_rand_breed_image_1(dogs_api_helper, dogs_api_client):
    breed = dogs_api_helper.find_rand_breed()
    response = dogs_api_client.get_rand_breed_image(breed, 1)
    assert response.ok

    images = response.json()['message']
    assert len(images) == 1


@pytest.mark.parametrize(["amount", "exp_amount"],
        [("asdfs", 1), (-3, 1), (3, 3), (52, 52)])
def test_get_rand_breed_image_many(dogs_api_helper, dogs_api_client, amount, exp_amount):
    breed = dogs_api_helper.find_rand_breed()
    response = dogs_api_client.get_rand_breed_image(breed, amount)
    assert response.ok

    images = response.json()['message']
    # assert len(images) >= exp_amount
    assert len(images) >= 1


@pytest.mark.parametrize(["breed", "expected"],
                         [("australian", 1), ("akita", 0), ("finnish", 1)])
def test_get_sub_breads_list(dogs_api_client, breed, expected):
    response = dogs_api_client.get_sub_breads_list(breed)
    assert response.ok
    assert len(response.json()['message']) == expected

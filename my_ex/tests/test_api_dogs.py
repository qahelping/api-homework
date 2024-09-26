import pytest

from my_ex.models.dog_api import DogApiResponse, DogApiListResponse
from my_ex.services.dog_service import DogService

LIST_OF_BREEDS = [
    "affenpinscher",
    "african",
    "airedale",
    "akita",
    "appenzeller",
    "basenji",
    "chihuahua",
]


def test_get_list_all_breeds():
    dog_api = DogService()
    response = dog_api.get_all_breads()
    assert "affenpinscher" in response.get('message')
    assert "australian" in response.get('message')
    assert "boxer" in response.get('message')
    assert "afghan" in response.get('message')['hound']


def test_get_random_image():
    dog_api = DogService()
    dog_api_response: DogApiResponse = dog_api.get_random_image()
    assert 'https://images.dog.ceo/breeds/' in dog_api_response.message


@pytest.mark.parametrize("breed", LIST_OF_BREEDS)
def test_get_all_images_from_breed(breed):
    dog_api = DogService()
    dog_api_response: DogApiListResponse = dog_api.get_all_images_from_breed(breed)
    assert 'https://images.dog.ceo/breeds/' in dog_api_response.message[0]


def test_get_all_sub_breed_from_existing_breed():
    dog_api = DogService()
    dog_api_response: DogApiListResponse = dog_api.get_all_sub_breed('hound')
    list_of_sub_breed = [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"
    ]
    assert list_of_sub_breed == dog_api_response.message


def test_get_all_sub_breed_from_non_existing_breed():
    dog_api = DogService()
    dog_api_response: DogApiListResponse = dog_api.get_all_sub_breed('123', is_negative=True)
    assert 'Breed not found (master breed does not exist)' == dog_api_response.message

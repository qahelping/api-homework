from my_ex.helpers.base_service import BaseService
from my_ex.models.dog_api import DogApiResponse, DogApiListResponse


class DogService(BaseService):
    def __init__(self):
        self.base_url = 'https://dog.ceo/api'

    def get_all_breads(self):
        return self.get(f"{self.base_url}/breeds/list/all")

    def get_random_image(self):
        response = self.get(f"{self.base_url}/breeds/image/random")
        return DogApiResponse(**response)

    def get_all_images_from_breed(self, breed):
        response = self.get(f"{self.base_url}/breed/{breed}/images")
        return DogApiListResponse(**response)

    def get_all_sub_breed(self, sub_breed, is_negative=False, code=404):
        if is_negative:
            response = self.get(f"{self.base_url}/breed/{sub_breed}/list", code=code)
            return DogApiResponse(**response)
        else:
            response = self.get(f"{self.base_url}/breed/{sub_breed}/list")
            return DogApiListResponse(**response)

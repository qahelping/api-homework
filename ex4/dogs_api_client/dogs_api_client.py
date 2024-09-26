"""
https://dog.ceo/dog-api/ client and testing

get_ methods are for external sources
find_ methods are for local search and selection
"""
import requests

class DogsApiClient:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = "https://dog.ceo/api"

    def get_all_breeds(self):
        """
        LIST ALL BREEDS
        :return: json
        {
        "message": {
            "affenpinscher": [], etc
        status success
        """
        url = f"{self.base_url}/breeds/list/all"
        response = self.session.get(url=url)
        return response

    def get_rand_images(self, amount=1):
        """
        DISPLAY SINGLE RANDOM IMAGE FROM ALL DOGS COLLECTION
        :param amount: DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION
        :return: json
        message str | list
        status success
        """
        url = f"{self.base_url}/breeds/image/random"
        if amount != 1:
            url = f"{url}/{amount}"
        response = self.session.get(url)
        return response

    def get_breed_images(self, breed):
        """
        Returns an array of all the images from a breed, e.g. hound
        :param breed: breed
        :return:
        message list,
        status success
        """
        url = f"{self.base_url}/breed/{breed}/images"
        response = self.session.get(url)
        return response

    def get_rand_breed_image(self, breed, amount=1):
        """
        RANDOM IMAGE FROM A BREED COLLECTION
        :param breed:
        :param amount:
        :return: json
        message str | list
        status success
        """
        url = f"{self.base_url}/breed/{breed}/images/random/{amount}"
        response = self.session.get(url)
        return response

    def get_sub_breads_list(self, breed):
        """
        Returns an array of all the sub-breeds from a breed
        :param breed:
        :return: :return: json
        message  list
        status success
        """
        url = f"{self.base_url}/breed/{breed}/list"
        response = self.session.get(url)
        return response

    def get_sub_bread_all_images(self, breed, sub):
        """
        LIST ALL SUB-BREED IMAGES
        :param breed:
        :param sub:
        :return:
        """
        url = f"{self.base_url}/breed/{breed}/{sub}/list/images"
        response = self.session.get(url)
        return response

    def get_sub_bread_rand_images(self, breed, sub, amount=1):
        """
        SINGLE RANDOM IMAGE FROM A SUB BREED COLLECTION
        :param breed:
        :param sub:
        :param amount: MULTIPLE IMAGES FROM A SUB-BREED COLLECTION
        :return:
        """
        url = f"{self.base_url}/breed/{breed}/{sub}/list/images/random"
        if amount != 1 and isinstance(amount, int) and 1 < amount <= 50:
            url = f"{url}/{amount}"
        response = self.session.get(url)
        return response

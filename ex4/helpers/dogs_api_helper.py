import random
from dogs_api_client.dogs_api_client import DogsApiClient


class DogsApiHelper:

    def __init__(self, client):
        self.all_breeds = client.get_all_breeds().json()['message']

    def find_rand_breed(self):
        """
        :param breeds: all breeds list, dictionary
        :return:  random key
        """
        breed = random.choice(list(self.all_breeds.keys()))
        return breed

    def find_breeds_with_sub(self):
        """
        :return: list of breeds with sub breeds
        """
        breeds = self.all_breeds
        breeds_extended = []
        for k, v in breeds.items():
            if len(v):
                breeds_extended.append(k)

        return breeds_extended

    def find_rand_sub_breed(self):
        """
        choose 1 random sub-breed
        """
        all_breeds = self.find_breeds_with_sub()
        rand_breed = random.choice(all_breeds)
        rand_sub_breed = random.choice(all_breeds[rand_breed])
        return rand_sub_breed

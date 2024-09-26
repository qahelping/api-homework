import requests


class BreweryApiClient:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/v1/"
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}

    def get_breweries_list(self):
        response = self.session.get(url=f"{self.base_url}breweries")
        return response

    def get_breweries_by_type(self, type, perpage):
        self.session.params = {"by_type": type, "per_page": perpage}
        response = self.session.get(url=f"{self.base_url}breweries")
        return response

    def get_rand_brewery(self, size = 0):
        if size:
            self.session.params = {"size": size}
        response = self.session.get(url=f"{self.base_url}breweries/random")
        return response



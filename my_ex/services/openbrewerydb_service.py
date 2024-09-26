from my_ex.helpers.base_service import BaseService
from my_ex.models.brewery import BreweryResponse, MetaResponse


class OpenBreweryDBService(BaseService):
    def __init__(self):
        self.base_url = 'https://api.openbrewerydb.org/v1'

    def get_breweries(self, id):
        return BreweryResponse(**self.get(f"{self.base_url}/breweries/{id}"))

    def get_country_breweries_meta_data(self, country):
        params = {'by_country': country}
        return MetaResponse(**self.get(f"{self.base_url}/breweries/meta", params=params))
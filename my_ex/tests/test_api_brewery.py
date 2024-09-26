import pytest

from my_ex.models.brewery import BreweryResponse, MetaResponse
from my_ex.services.openbrewerydb_service import OpenBreweryDBService


def test_get_breweries():
    api = OpenBreweryDBService()
    uid = 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'
    breweries = api.get_breweries(uid)
    assert breweries.id_ == uid


def test_get_country_breweries_meta_data():
    api = OpenBreweryDBService()
    meta = api.get_country_breweries_meta_data('south_korea')
    assert meta.total == '61'
    assert meta.page == '1'
    assert meta.per_page == '50'

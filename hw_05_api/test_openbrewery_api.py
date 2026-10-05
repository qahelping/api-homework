import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"


def test_get_single_brewery():
    # brewery_id="b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    #получаем список пивоварен
    list_response = requests.get(BASE_URL, params={"per_page": 1})
    assert list_response.status_code == 200
    # список не пустой, проверка
    breweries = list_response.json()
    assert len(breweries) > 0
    #берем первую
    brewery_id = breweries[0]["id"]
    response = requests.get(f"{BASE_URL}/{brewery_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == brewery_id
    assert "name" in data
    assert "brewery_type" in data
    assert "city" in data
    assert "country" in data


def test_get_list_breweries():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_random_brewery():
    response = requests.get(f"{BASE_URL}/random")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    brewery = data[0]
    assert "id" in brewery
    assert "name" in brewery
    assert "brewery_type" in brewery
    assert "city" in brewery
    assert "country" in brewery


@pytest.mark.parametrize("size", [1, 2, 3])
def test_get_random_brewery_with_size(size):
    response = requests.get(f"{BASE_URL}/random", params={"size": size})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == size
    for brewery in data:
        assert "id" in brewery
        assert "name" in brewery
        assert "brewery_type" in brewery
        assert "city" in brewery
        assert "country" in brewery


@pytest.mark.parametrize("query", ["G8 Development, Inc.", "Deft Brewing", "District 14"])
def test_search_breweries(query):
    response = requests.get(f"{BASE_URL}/search", params={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    found = False
    for brewery in data:
        if query.lower() in brewery["name"].lower():
            found = True
    assert found


@pytest.mark.parametrize("per_page", [1, 2, 5])
def test_search_breweries_per_page(per_page):
    response = requests.get(
        f"{BASE_URL}/search",
        params={"query": "brew", "per_page": per_page},
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= per_page
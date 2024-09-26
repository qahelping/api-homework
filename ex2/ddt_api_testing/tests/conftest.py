import pytest
from ex2.ddt_api_testing.utils.base_request import BaseSession
import os
from dotenv import load_dotenv

load_dotenv()
URL_JSONPLACEHOLDER = os.getenv("BASE_URL_JSONPLACEHOLDER")
URl_DOG_API = os.getenv("BASE_URl_DOG_API")
URl_DOG_API2 = os.getenv("BASE_URl_DOG_API2")
URl_Brewery = os.getenv("BAS_URl_Brewery")


@pytest.fixture(scope="function")
def jsonplaceholder_api():
    jsonplaceholder_session = BaseSession(URL_JSONPLACEHOLDER)
    return jsonplaceholder_session


@pytest.fixture(scope="function")
def dog_api():
    dog_session = BaseSession(URl_DOG_API)
    dogs_session = BaseSession(URl_DOG_API2)
    return dog_session, dogs_session


@pytest.fixture(scope="function")
def brewery_api():
    brewery_session = BaseSession(URl_Brewery)
    return brewery_session

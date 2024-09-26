import pytest


# doc https://docs.pytest.org/en/7.1.x/example/simple.html
def pytest_addoption(parser):
    parser.addoption("--actual", default="https://ya.ru", type=str, help="Actual url")

    parser.addoption("--expected", default=200, type=int, help="Expected status code")


@pytest.fixture
def url(request):
    return request.config.getoption("--actual")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--expected")

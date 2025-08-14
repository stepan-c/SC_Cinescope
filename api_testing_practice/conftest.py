#conftest.py
import pytest
import requests
from api_testing_practice.api.api_manager import ApiManager

@pytest.fixture()
def api_manager():
    session = requests.Session()
    a = ApiManager(session)
    a.auth_api.auth()

    return a


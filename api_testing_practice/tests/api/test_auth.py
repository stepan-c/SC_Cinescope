#test_auth
from api_testing_practice.api.auth_api import AuthAPI
from api_testing_practice.utils.data_generator import DataGenerator
import requests
import pytest

def test_register_user():
    session = requests.Session()
    auth_api = AuthAPI(session)

    user_data = DataGenerator.generate_user_data()

    response = auth_api.register_user(user_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201

def test_login_admin():
    session = requests.Session()
    auth_api = AuthAPI(session)

    response = auth_api.login_admin()

    assert response.status_code == 200
    body = response.json()
    assert "accessToken" in body
    return body["accessToken"]




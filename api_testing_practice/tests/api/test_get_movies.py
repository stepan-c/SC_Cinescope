from api_testing_practice.api.movie_api import MoviesApi
from api_testing_practice.api.auth_api import AuthAPI
from api_testing_practice.constants import movies_data, fake_movies_data
import requests
import pytest

def test_get_movies():
    session = requests.Session()

    auth_api = AuthAPI(session)
    response = auth_api.login_admin()

    movies_api = MoviesApi(session)
    response = movies_api.get_movies(movies_data=movies_data())

    assert response.status_code == 200

def test_get_fake_movies():
    session = requests.Session()

    auth_api = AuthAPI(session)
    response = auth_api.login_admin()

    movies_api = MoviesApi(session)
    response = movies_api.get_movies(movies_data=fake_movies_data())

    assert response.status_code in (400,401,404)




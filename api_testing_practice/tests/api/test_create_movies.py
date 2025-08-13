#test_create_movies.py
from api_testing_practice.api.movie_api import MoviesApi
from api_testing_practice.api.auth_api import AuthAPI
from api_testing_practice.constants import film_data
from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.api.api_manager import ApiManager
import requests
import pytest

def test_create_movies(api_manager):

    api_manager.movie_api.create_movies(movie_data=DataGenerator.generator_film_data())

# def test_create_fake_movies():
#     session = requests.Session()
#     auth_api = AuthAPI(session)
#
#     response = auth_api.login_admin()
#     token = response.json()['accessToken']
#
#     movie_api = MoviesApi(session)
#     movie_api.headers['Authorization'] = f"Bearer {token}"
#
#     response = movie_api.create_movies(movie_data=film_data())
#     assert response.status_code in (400,401,409)
#     print("Фильм не создан, название уже занято!")




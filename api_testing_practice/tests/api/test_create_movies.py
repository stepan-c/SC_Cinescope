#test_create_movies.py
from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.api.api_manager import ApiManager
from api_testing_practice.conftest import api_manager
import requests
import pytest

def test_create_movies(api_manager):
    api_manager.movie_api.create_movies(movie_data=DataGenerator.generator_film_data())

    movie_id = api_manager.movie_api.last_created_movie_id
    print(f"Создан фильм с id: {movie_id}")


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




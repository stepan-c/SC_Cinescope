from api_testing_practice.api.movie_api import MoviesApi
from api_testing_practice.api.auth_api import AuthAPI
from api_testing_practice.api.api_manager import ApiManager
from api_testing_practice.constants import movies_data, fake_movies_data
from api_testing_practice.conftest import api_manager
import requests
import pytest

from api_testing_practice.utils.data_generator import DataGenerator


# def test_get_movies():
#     session = requests.Session()
#
#     auth_api = AuthAPI(session)
#     response = auth_api.login_admin()
#
#     movies_api = MoviesApi(session)
#     response = movies_api.get_movies(movies_data=movies_data())
#
#     assert response.status_code == 200


# def test_get_last_movies_from_id(api_manager):
#     api_manager.movie_api.create_movies(movie_data=DataGenerator.generator_film_data())
#
#     get_resp = api_manager.movie_api.get_movies_from_id(api_manager.movie_api.last_created_movie_id)
#
#     assert get_resp.json()["id"] == api_manager.movie_api.last_created_movie_id
#
#     print(get_resp.json())


def test_get_movie_from_id(api_manager):
    movie_id = 8975

    get_movie = api_manager.movie_api.get_movies_from_id(movie_id=movie_id)

    assert get_movie.status_code == 200
    assert get_movie.json()['id'] == movie_id
    print(get_movie.json())

#Негативный тест
def test_get_fake_movies_from_id(api_manager):
    movie_id = 9999

    get_fake_movie = api_manager.movie_api.get_movies_from_id(movie_id=movie_id, expected_status=404)












#conftest.py
import pytest
import requests
from api_testing_practice.api.api_manager import ApiManager
from api_testing_practice.utils.data_generator import DataGenerator


@pytest.fixture()
def api_manager():
    session = requests.Session()
    a = ApiManager(session)
    a.auth_api.auth()

    return a

@pytest.fixture()
def create_movie(api_manager):
    random_data = DataGenerator.generator_film_data()
    response = api_manager.movie_api.create_movies(movie_data=random_data)
    create_movie_id = response.json()['id']
    return create_movie_id


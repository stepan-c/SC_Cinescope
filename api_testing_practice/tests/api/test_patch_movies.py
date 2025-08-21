from api_testing_practice.conftest import api_manager
from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.conftest import create_movie


def test_patch_movies(api_manager,create_movie):

    response = api_manager.movie_api.patch_movies(movie_id=create_movie, movie_data=DataGenerator.patch_movie_data()).json()

    assert response.get('name') != api_manager.movie_api.get_movies(movie_id=create_movie)

def test_patch_fake_movies(api_manager, create_movie):

    api_manager.movie_api.patch_movies(movie_id=create_movie,movie_data=DataGenerator.patch_fake_movie_data(), expected_status=400)

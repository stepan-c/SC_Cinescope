from api_testing_practice.conftest import api_manager
from api_testing_practice.utils.data_generator import DataGenerator


def test_patch_movies(api_manager):
    movie_id = 9421

    response = api_manager.movie_api.patch_movies(movie_id=movie_id, movie_data=DataGenerator.patch_movie_data()).json()

    assert response.get('name') != api_manager.movie_api.get_movies(movie_id=movie_id)
    print(response)

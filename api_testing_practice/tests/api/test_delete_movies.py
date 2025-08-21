from api_testing_practice.conftest import api_manager
from api_testing_practice.conftest import create_movie


def test_del_movies(api_manager, create_movie):
    response = api_manager.movie_api.delete_movies(movie_id=create_movie).json()
    assert response.get('id') == create_movie


def test_del_fake_movies(api_manager, create_movie):
    api_manager.movie_api.delete_movies(movie_id=create_movie,expected_status=200)
    api_manager.movie_api.delete_movies(movie_id=create_movie,expected_status=404)

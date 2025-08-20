from api_testing_practice.conftest import api_manager
from api_testing_practice.utils.data import filter_data,fake_filter_data


def test_get_movie_from_id(api_manager):
    movie_id = 9420

    get_movie = api_manager.movie_api.get_movies(movie_id=movie_id).json()

    assert get_movie['id'] == movie_id


def test_get_fake_movies_from_id(api_manager):
    movie_id = 9999

    api_manager.movie_api.get_movies(movie_id=movie_id, expected_status=404)


def test_filter_movies(api_manager):
    api_manager.movie_api.get_movies(params=filter_data())


def test_fake_filter_movies(api_manager):
    api_manager.movie_api.get_movies(params=fake_filter_data(), expected_status=400)










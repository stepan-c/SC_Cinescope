from api_testing_practice.conftest import api_manager
from api_testing_practice.utils.data import filter_data,fake_filter_data
import pytest


@pytest.mark.parametrize("params,expected_status",
                        [(filter_data(), 200),
                        (fake_filter_data(), 400)],
                        ids=['Позитивный тест', 'Негативный тест'])
def test_filter(api_manager, params, expected_status):

    api_manager.movie_api.get_movies(params=params, expected_status=expected_status)


def test_get_movie_from_id(api_manager, admin):
    movie_id = 9420

    get_movie = admin.api.movie_api.get_movies(movie_id=movie_id).json()

    assert get_movie['id'] == movie_id


@pytest.mark.slow
def test_get_fake_movies_from_id(api_manager, admin):
    movie_id = 9999

    admin.api.movie_api.get_movies(movie_id=movie_id, expected_status=404)










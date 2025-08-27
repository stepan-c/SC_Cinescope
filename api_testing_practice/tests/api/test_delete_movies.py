from api_testing_practice.conftest import api_manager, super_admin
from api_testing_practice.conftest import create_movie
import pytest

def test_del_movies(api_manager, create_movie, super_admin):
    response = super_admin.api.movie_api.delete_movies(movie_id=create_movie).json()
    assert response.get('id') == create_movie


def test_del_fake_movies(api_manager, create_movie, super_admin):
    super_admin.api.movie_api.delete_movies(movie_id=create_movie,expected_status=200)
    super_admin.api.movie_api.delete_movies(movie_id=create_movie,expected_status=404)

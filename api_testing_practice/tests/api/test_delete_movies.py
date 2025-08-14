from api_testing_practice.conftest import api_manager
import requests
import pytest

def test_del_movies(api_manager):
    movie_id = 8972
    response = api_manager.movie_api.get_movies_from_id(movie_id=movie_id)

    assert response.status_code == 200
    assert response.json()['id'] == movie_id
    print(f"Фильм с id:{movie_id} был удален")

def test_del_fake_movies(api_manager):
    movie_id = 9999
    response = api_manager.movie_api.get_movies_from_id(movie_id,expected_status=404)

import pytest
import requests
from api_testing_practice.conftest import api_manager
from api_testing_practice.constants import patch_movie_data

def test_patch_movies(api_manager):
    movie_id = 8975

    response = api_manager.movie_api.patch_movies(movie_id=movie_id,data=patch_movie_data())

    assert response.status_code == 200
    print(response.json())

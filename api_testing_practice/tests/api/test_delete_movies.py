from api_testing_practice.conftest import api_manager

movie_id = 9419

def test_del_movies(api_manager):
    response = api_manager.movie_api.delete_movies(movie_id=movie_id).json()
    assert response.get('id') == movie_id


def test_del_fake_movies(api_manager):
    api_manager.movie_api.delete_movies(movie_id,expected_status=404)

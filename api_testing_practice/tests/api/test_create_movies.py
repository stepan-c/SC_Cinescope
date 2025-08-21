from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.conftest import api_manager


def test_create_movies(api_manager):
    random_data = DataGenerator.generator_film_data()

    s = api_manager.movie_api.create_movies(movie_data=random_data)
    movie_id = s.json()['id']

    assert movie_id, f"Фильм не создан, ошибка:{s.status_code}"
    print(f"Создан фильм с id: {movie_id}")


def test_create_fake_movies(api_manager):
    fake_data = DataGenerator.generator_fake_film_data()

    api_manager.movie_api.create_movies(movie_data=fake_data,expected_status=400)

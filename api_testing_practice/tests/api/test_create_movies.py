from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.conftest import api_manager


def test_create_movies(api_manager):
    random_data = DataGenerator.generator_film_data()

    s = api_manager.movie_api.create_movies(movie_data=random_data)
    movie_id = s.json()['id']

    assert movie_id, f"Фильм не создан, ошибка:{s.status_code}"
    print(f"Создан фильм с id: {movie_id}")



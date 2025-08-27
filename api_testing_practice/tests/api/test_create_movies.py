from api_testing_practice.utils.data_generator import DataGenerator
import pytest


@pytest.mark.slow
def test_create_movies(api_manager, super_admin):
    random_data = DataGenerator.generator_film_data()

    s = super_admin.api.movie_api.create_movies(movie_data=random_data)
    movie_id = s.json()['id']

    assert movie_id, f"Фильм не создан, ошибка:{s.status_code}"
    print(f"Создан фильм с id: {movie_id}")


def test_create_fake_movies(api_manager, admin):
    fake_data = DataGenerator.generator_fake_film_data()

    admin.api.movie_api.create_movies(movie_data=fake_data,expected_status=400)

@pytest.mark.slow
def test_create_movies_by_user(common_user,api_manager):
    random_data = DataGenerator.generator_film_data()

    common_user.api.movie_api.create_movies(movie_data=random_data,expected_status=403)


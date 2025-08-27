#api_manager.py
from api_testing_practice.api.movie_api import MoviesApi
from api_testing_practice.api.auth_api import AuthAPI
from api_testing_practice.api.user_api import UserApi
from api_testing_practice.constants import ADMIN_DATA


class ApiManager:
    def __init__(self, session):
        self.auth_api = AuthAPI(session)
        self.movie_api = MoviesApi(session)
        self.user_api = UserApi(session)
        self.session = session

    def close_session(self):
        self.session.close()


if __name__ == "__main__":
    import requests
    from api_testing_practice.utils.data_generator import DataGenerator

    session = requests.Session()
    a = ApiManager(session)
    token = a.auth_api.login_user(login_data=ADMIN_DATA).json()['accessToken']

    a.session.headers.update({'Authorization': f"Bearer {token}"})
    b = a.movie_api.create_movies(movie_data=DataGenerator.generator_film_data())
    assert b.status_code == 201



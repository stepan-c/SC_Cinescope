from api_testing_practice.api.movie_api import MoviesApi
from api_testing_practice.api.auth_api import AuthAPI

class ApiManager():
    def __init__(self, session):
        self.auth_api = AuthAPI(session)
        self.movie_api = MoviesApi(session)
        self.session = session


if __name__ == "__main__":
    import requests
    from api_testing_practice.utils.data_generator import DataGenerator

    session = requests.Session()
    a = ApiManager(session)
    token = a.auth_api.login_admin().json()['accessToken']

    a.session.headers.update({'Authorization': f"Bearer {token}"})
    b = a.movie_api.create_movies(movie_data=DataGenerator.generator_film_data())
    assert b.status_code == 201



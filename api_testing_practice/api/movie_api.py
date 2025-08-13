#movie_api.py
from api_testing_practice.custom_requester.custom_requester import CustomRequester
from api_testing_practice.constants import CREATE_URL, MOVIES_ENDPOINT

class MoviesApi(CustomRequester):
    def __init__(self,session):
        super().__init__(session=session,base_url=CREATE_URL)

    def create_movies(self, movie_data, expected_status=201):
        return self.send_request(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            data=movie_data,
            expected_status= expected_status
        )

    def get_movies(self, movies_data):
        return self.send_request(
            method="GET",
            endpoint=MOVIES_ENDPOINT,
            data=movies_data,
            expected_status=200
        )



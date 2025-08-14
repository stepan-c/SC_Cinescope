#movie_api.py
from api_testing_practice.custom_requester.custom_requester import CustomRequester
from api_testing_practice.constants import CREATE_URL, MOVIES_ENDPOINT, movies_data, patch_movie_data


class MoviesApi(CustomRequester):
    def __init__(self,session):
        super().__init__(session=session,base_url=CREATE_URL)

    def create_movies(self, movie_data, expected_status=201):
        response = self.send_request(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            data=movie_data,
            expected_status=expected_status
        )

        # сохраняем id созданного фильма
        self.last_created_movie_id = response.json().get("id")
        return response

    def get_movies(self):
        return self.send_request(
            method="GET",
            endpoint=MOVIES_ENDPOINT,
            data=movies_data,
            expected_status=200
        )

    def get_movies_from_id(self, movie_id, expected_status=200):
        return self.send_request_from_id(
            method="GET",
            endpoint=MOVIES_ENDPOINT,
            movie_id=movie_id,
            expected_status=expected_status
        )

    def patch_movies(self,movie_id, data, expected_status=200):
        return self.send_request_from_id(
            method="PATCH",
            endpoint=MOVIES_ENDPOINT,
            movie_id=movie_id,
            data=patch_movie_data()
        )




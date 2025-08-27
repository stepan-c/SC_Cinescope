#user_api.py
from api_testing_practice.custom_requester.custom_requester import CustomRequester
from api_testing_practice.constants import BASE_URL,USER_ENDPOINT


class UserApi(CustomRequester):
    def __init__(self,session):
        super().__init__(session,BASE_URL)

    def get_user(self,user_location,expected_status=200):
        return self.send_request(
            method='GET',
            endpoint=USER_ENDPOINT+f'/{user_location}',
            expected_status=expected_status
        )

    def create_user(self,user_data, expected_status=201):
        return self.send_request(
            method='POST',
            endpoint=USER_ENDPOINT,
            data=user_data,
            expected_status=expected_status
        )
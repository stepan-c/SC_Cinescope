#auth_api
from api_testing_practice.custom_requester.custom_requester import CustomRequester
from api_testing_practice.constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT, BASE_URL, ADMIN_DATA

class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def register_user(self, user_data):
        return self.send_request(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=user_data,
            expected_status=201
        )

    def login_user(self, login_data):
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=200
        )

    def login_admin(self):
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=ADMIN_DATA,
            expected_status=200
        )


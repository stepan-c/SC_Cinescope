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


    def auth(self, creds=None):
        if creds:
            login_data = {
            "email": creds[0],
            "password": creds[1]
            }
        else:
            login_data = ADMIN_DATA
        token = self.login_user(login_data=login_data).json()['accessToken']
        self.session.headers.update({'Authorization': f"Bearer {token}"})


from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.constants import ADMIN_DATA
from api_testing_practice.conftest import api_manager


def test_register_user(api_manager,common_user):

    user_data = DataGenerator.generate_user_data()

    common_user.api.auth_api.register_user(user_data)


def test_login_admin(api_manager,admin):

    response = admin.api.auth_api.login_user(login_data=ADMIN_DATA)

    assert response.status_code == 200
    body = response.json()
    assert "accessToken" in body
    return body["accessToken"]




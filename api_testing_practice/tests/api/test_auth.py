from api_testing_practice.constants import ADMIN_DATA
from api_testing_practice.conftest import api_manager
import pytest


@pytest.mark.slow
def test_register_user(registered_user, test_user):
    assert registered_user.email == test_user.email, "Email не совпадает"


def test_login_admin(api_manager,admin):

    response = admin.api.auth_api.login_user(login_data=ADMIN_DATA)

    assert response.status_code == 200
    body = response.json()
    assert "accessToken" in body
    return body["accessToken"]




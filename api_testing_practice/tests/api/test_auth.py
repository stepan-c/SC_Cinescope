from api_testing_practice.constants import ADMIN_DATA
from api_testing_practice.conftest import api_manager, test_user, db_session
import pytest

from api_testing_practice.models.base_models import TestUser, RegisterUserResponse
from db_requester.models import UserDBModel


@pytest.mark.slow
def test_register_user(registered_user, test_user):
    assert registered_user.email == test_user.email, "Email не совпадает"


def test_login_admin(api_manager,admin):

    response = admin.api.auth_api.login_user(login_data=ADMIN_DATA)

    assert response.status_code == 200
    body = response.json()
    assert "accessToken" in body
    return body["accessToken"]


def test_register_user_db_session(api_manager, test_user: TestUser, db_session):
    session, test_db_user = db_session  # ← распаковываем кортеж

    # Преобразуйте TestUser в словарь перед отправкой
    response = api_manager.auth_api.register_user(test_user.model_dump())

    register_user_response = RegisterUserResponse(**response.json())

    # Проверяем добавил ли сервис Auth нового пользователя в базу данных
    users_from_db = session.query(UserDBModel).filter(
        UserDBModel.id == register_user_response.id)  # ← используем session

    # получили обьект из бзы данных и проверили что он действительно существует в единственном экземпляре
    assert users_from_db.count() == 1, "обьект не попал в базу данных"

    # Достаем первый и единственный обьект из списка полученных
    user_from_db = users_from_db.first()

    # можем осуществить проверку всех полей в базе данных например Email
    assert user_from_db.email == test_user.email, "Email не совпадает"


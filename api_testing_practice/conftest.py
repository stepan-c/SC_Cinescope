#conftest.py
import pytest
import requests
from api_testing_practice.api.api_manager import ApiManager
from api_testing_practice.models.base_models import TestUser, RegisterUserResponse
from api_testing_practice.utils.data_generator import DataGenerator
from api_testing_practice.utils.data import SuperAdminCreds
from api_testing_practice.utils.roles import Roles
from entities.user import User


@pytest.fixture()
def api_manager():
    session = requests.Session()
    a = ApiManager(session)
    a.auth_api.auth()

    return a

@pytest.fixture()
def create_movie(api_manager):
    random_data = DataGenerator.generator_film_data()
    response = api_manager.movie_api.create_movies(movie_data=random_data)
    create_movie_id = response.json()['id']
    return create_movie_id

@pytest.fixture()
def test_user() -> TestUser:
    random_password = DataGenerator.password_generator()
    return TestUser(
        email=DataGenerator.generator_email(),
        fullName=DataGenerator.name_generator(),
        password=random_password,
        passwordRepeat=random_password,
        roles=[Roles.USER]
    )


@pytest.fixture()
def registered_user(api_manager, test_user):
    user_data = test_user.model_dump()
    user_data.update({
        "verified": True,
        "banned": False
    })
    response = api_manager.auth_api.register_user(user_data=user_data)
    return RegisterUserResponse(**response.json())


@pytest.fixture()
def created_user(super_admin, test_user):
    user_data = test_user.model_dump()
    user_data.update({
        "verified": True,
        "banned": False
    })

    response = super_admin.api.user_api.create_user(user_data)
    return response.json()

@pytest.fixture()
def user_session():
    user_pool = []

    def _create_user_session():
        session = requests.Session()
        user_session = ApiManager(session)
        user_pool.append(user_session)
        return user_session

    yield _create_user_session

    for user in user_pool:
        user.close_session()

@pytest.fixture()
def super_admin(user_session):
    new_session = user_session()

    super_admin = User(
        SuperAdminCreds.USERNAME,
        SuperAdminCreds.PASSWORD,
        list(Roles.SUPER_ADMIN.value),
        new_session
    )
    super_admin.api.auth_api.auth(super_admin.creds)
    return super_admin

@pytest.fixture()
def admin(user_session):
    new_session = user_session()

    admin = User(
        SuperAdminCreds.USERNAME,
        SuperAdminCreds.PASSWORD,
        list(Roles.ADMIN.value),
        new_session
    )
    admin.api.auth_api.auth(admin.creds)
    return admin

@pytest.fixture(scope='function')
def create_super_user(test_user):
    new_data = test_user.model_dump()
    new_data.update({
        "verified": True,
        "banned": False
    })
    return new_data

@pytest.fixture()
def common_user(user_session,super_admin,create_super_user):
    new_session = user_session()

    common_user = User(
        create_super_user['email'],
        create_super_user['password'],
        list(Roles.USER.value),
        new_session
    )

    super_admin.api.user_api.create_user(create_super_user)
    common_user.api.auth_api.auth(common_user.creds)
    return common_user







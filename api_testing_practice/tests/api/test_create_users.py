#test_create_users.py
import pytest


class TestUser:

    def test_create_user(self, created_user, test_user):

        assert created_user.get('id') != ''
        assert created_user.get('verified') == True
        assert created_user.get('email') == test_user.email

    @pytest.mark.slow
    def test_get_user_by_location(self, super_admin, created_user, test_user):
        s = super_admin.api.user_api.get_user(user_location=created_user['email']).json()

        assert s.get('id') != ''
        assert s.get('email') == test_user.email

    def test_get_user_by_id_common_user(self, common_user):
        common_user.api.user_api.get_user(common_user.email, expected_status=403)




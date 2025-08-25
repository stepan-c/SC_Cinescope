#test_create_users.py
class TestUser:

    def test_create_user(self,super_admin,create_super_user):
        a = super_admin.api.user_api.create_user(create_super_user).json()

        assert a.get('id') != ''
        assert a.get('verified') == True
        assert a.get('email') == create_super_user['email']

    def test_get_user_by_location(self, super_admin, create_user_data):
        s = super_admin.api.user_api.get_user(user_location=create_user_data['email']).json()

        assert s.get('id') != ''
        assert s.get('email') == create_user_data['email']

    def test_get_user_by_id_common_user(self, common_user):
        common_user.api.user_api.get_user(common_user.email, expected_status=403)




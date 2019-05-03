import unittest
import json
from app import app, db


class AuthTestCase(unittest.TestCase):
    """Test case for the authentication blueprint."""

    def setUp(self):
        """Set up test variables."""
        self.app = app
        self.user_data = {'username': 'test_user',
                          'password': 'test_password'}
        with self.app.app_context(), open('../epytodo.sql', 'r') as f:
            db.session.close()
            db.engine.execute(f.read())

    def test_registration(self):
        """Test user registration works correcty."""
        res = self.client().post('/register', data=self.user_data)
        result = json.loads(res.data.decode())

        self.assertEqual(result, app.config['REGISTER_RES'])

    def test_already_registered_user(self):
        """Test that a user cannot be registered twice."""
        res = self.client().post('/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)

        second_res = self.client().post('/register', data=self.user_data)
        self.assertEqual(second_res, )

        result = json.loads(second_res.data.decode())
        self.assertEqual(result, app.config['REGISTER_ERR'])

    def test_user_login(self):
        """Test registered user can login."""
        res = self.client().post('/register', data=self.user_data)
        self.assertEqual(res.status_code, 201)

        login_res = self.client().post('/signin', data=self.user_data)
        result = json.loads(login_res.data.decode())

        self.assertEqual(result, app.config['SIGNIN_RES'])

    def test_non_registered_user_login(self):
        """Test non registered users cannot login."""
        not_a_user = {'username': 'not_a_user',
                      'password': 'nope'}
        res = self.client().post('/signin', data=not_a_user)
        result = json.loads(res.data.decode())

        self.assertEqual(result, app.config['SIGNIN_ERR'])


if __name__ == "__main__":
    unittest.main()

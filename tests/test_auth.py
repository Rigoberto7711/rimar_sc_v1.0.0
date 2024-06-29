import unittest
from app import create_app, db
from app.blueprints.auth.models import User
from flask import url_for
from config import TestConfig

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_login_logout(self):
        with self.app.test_request_context():
            # Register a new account
            response = self.client.post(url_for('auth.register'), data={
                'username': 'test',
                'email': 'test@example.com',
                'password': 'password',
                'password2': 'password',
                'agency': 'Wiwili3',
                'role': 'usuario',
                'submit': True
            })
            self.assertEqual(response.status_code, 302)

            # Login with the new account
            response = self.client.post(url_for('auth.login'), data={
                'username': 'test',
                'password': 'password',
                'submit': True
            })
            self.assertEqual(response.status_code, 302)

            # Logout
            response = self.client.get(url_for('auth.logout'))
            self.assertEqual(response.status_code, 302)

    def test_change_password(self):
        with self.app.test_request_context():
            # Create a user
            user = User(username='test', email='test@example.com', agency='Wiwili3', role='usuario')
            user.set_password('password')
            db.session.add(user)
            db.session.commit()

            # Login
            self.client.post(url_for('auth.login'), data={
                'username': 'test',
                'password': 'password',
                'submit': True
            })

            # Change password
            response = self.client.post(url_for('auth.change_password'), data={
                'old_password': 'password',
                'new_password': 'newpassword',
                'new_password2': 'newpassword',
                'submit': True
            })
            self.assertEqual(response.status_code, 302)

            # Logout
            self.client.get(url_for('auth.logout'))

            # Login with new password
            response = self.client.post(url_for('auth.login'), data={
                'username': 'test',
                'password': 'newpassword',
                'submit': True
            })
            self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()

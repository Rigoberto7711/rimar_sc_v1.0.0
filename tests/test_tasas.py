# tests/test_tasas.py

import unittest
from app import create_app, db
from app.blueprints.tasas.models import Tasa
from config import TestConfig

class TasasTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_tasas_creation(self):
        response = self.client.post('/tasas/', data={
            'name': 'Test Tasa'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        tasa = Tasa.query.filter_by(name='Test Tasa').first()
        self.assertIsNotNone(tasa)

if __name__ == '__main__':
    unittest.main()

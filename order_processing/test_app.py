
import unittest
from app import app, db
from models import Order
import requests_mock
from flask_jwt_extended import create_access_token


class OrderProcessingTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_orders.db'
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_order(self):
        # Generate JWT token
        with app.app_context():
            token = create_access_token(identity='test_user')

        with requests_mock.Mocker() as m:
            m.get(
                'http://localhost:9002/products/1',
                json={'id': 1, 'quantity': 10},
                status_code=200
            )
            m.put(
                'http://localhost:9002/products/1',
                json={'quantity': 9},
                status_code=200
            )

            # Send request with JWT authorization
            response = self.app.post(
                '/orders',
                json={'product_id': 1, 'quantity': 1},
                headers={'Authorization': f'Bearer {token}'}
            )

            self.assertEqual(response.status_code, 201)

            with app.app_context():
                self.assertEqual(Order.query.count(), 1)


if __name__ == '__main__':
    unittest.main()

import unittest
from app import app, db
from models import Product
from flask_jwt_extended import create_access_token

class ProductManagementTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_products.db'

        self.app = app.test_client()

        with app.app_context():
            db.create_all()
            token = create_access_token(identity='test_user')
            self.headers = {
                'Authorization': f'Bearer {token}'
            }

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_product(self):
        response = self.app.post(
            '/products',
            json={
                'name': 'Test Product',
                'description': 'Test Description',
                'price': 10.0,
                'quantity': 100
            },
            headers=self.headers
        )

        self.assertEqual(response.status_code, 201)

        with app.app_context():
            self.assertEqual(Product.query.count(), 1)

    def test_get_product(self):
        create_response = self.app.post(
            '/products',
            json={
                'name': 'Test Product',
                'description': 'Test Description',
                'price': 10.0,
                'quantity': 100
            },
            headers=self.headers
        )

        self.assertEqual(create_response.status_code, 201)

        response = self.app.get(
            '/products/1',
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Test Product')


if __name__ == '__main__':
    unittest.main()

import unittest
from app import app
from flask import Flask

class ProductServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_product(self):
        new_product = {"id": 3, "name": "Tablet", "price": 300}
        response = self.client.post('/products', json=new_product)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, new_product)

if __name__ == "__main__":
    unittest.main()

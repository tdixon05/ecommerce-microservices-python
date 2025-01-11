import unittest
from app import app
from flask import Flask

class UserServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_user(self):
        new_user = {"id": 3, "name": "Charlie"}
        response = self.client.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, new_user)

if __name__ == "__main__":
    unittest.main()

import unittest
import json
from REST_api import app, UserManager  # Import UserManager for resetting state

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset the global `users` list to its default state
        UserManager.reset_users()

    def test_get_all_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_get_user_by_id(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Alice')

    def test_get_user_not_found(self):
        response = self.app.get('/users/999')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'User not found')

    def test_create_user(self):
        new_user = {"name": "Charlie", "email": "charlie@example.com"}
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Charlie')

    def test_create_user_invalid(self):
        invalid_user = {"email": "missing_name@example.com"}
        response = self.app.post('/users', json=invalid_user)
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Name and email are required')

    def test_update_user(self):
        updated_user = {"name": "Alice Updated"}
        response = self.app.put('/users/1', json=updated_user)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Alice Updated')

    def test_update_user_not_found(self):
        updated_user = {"name": "Nonexistent User"}
        response = self.app.put('/users/999', json=updated_user)
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'User not found')

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User deleted')

    def test_delete_user_not_found(self):
        response = self.app.delete('/users/999')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User deleted')

if __name__ == '__main__':
    unittest.main()

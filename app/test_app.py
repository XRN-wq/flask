import unittest
import sqlite3
from flask_app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your index page content', response.data)  # Replace with expected content

    def test_list(self):
        response = self.app.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your list page content', response.data)  # Replace with expected content

    def test_get(self):
        response = self.app.get('/get')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your get page content', response.data)  # Replace with expected content

    def test_select_existing_row(self):
        response = self.app.post('/select', data={'var': '1'})
        self.assertIn(b'Expected result content', response.data)  # Replace with expected content

    def test_select_nonexistent_row(self):
        response = self.app.post('/select', data={'var': '9999'})
        self.assertIn(b'No such result found', response.data)

    def test_select_invalid_method(self):
        response = self.app.get('/select')
        self.assertEqual(response.status_code, 405)

    def test_delete_existing_row(self):
        response = self.app.post('/delete', data={'var': '1'})
        self.assertIn(b'Row was deleted', response.data)

    def test_delete_nonexistent_row(self):
        response = self.app.post('/delete', data={'var': '9999'})
        self.assertIn(b'Error!', response.data)

    def test_delete_get(self):
        response = self.app.get('/delete')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your delete page content', response.data)  # Replace with expected content

    def test_delete_invalid_method(self):
        response = self.app.get('/delete')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
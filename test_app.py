import unittest
from app.app import app, db

class WishAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_add_wish(self):
        response = self.app.post('/add_wish', json={'content': 'Test Wish 1'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Wish added successfully', response.get_json()['message'])

    def test_get_all_wishes(self):
        response = self.app.get('/wishes')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_like_wish(self):
        add_response = self.app.post('/add_wish', json={'content': 'Test Wish 2'})
        wish_id = add_response.get_json()['id']

        like_response = self.app.post(f'/wishes/{wish_id}/like')
        self.assertEqual(like_response.status_code, 200)
        self.assertIn('Wish liked successfully', like_response.get_json()['message'])

    def test_remove_wish(self):
        add_response = self.app.post('/add_wish', json={'content': 'Test Wish 3'})
        wish_id = add_response.get_json()['id']

        remove_response = self.app.delete(f'/wishes/{wish_id}')
        self.assertEqual(remove_response.status_code, 200)
        self.assertIn('Wish removed successfully', remove_response.get_json()['message'])

    def test_remove_all_wishes(self):
        self.app.post('/add_wish', json={'content': 'Test Wish 4'})
        self.app.post('/add_wish', json={'content': 'Test Wish 5'})

        remove_all_response = self.app.delete('/wishes')
        self.assertEqual(remove_all_response.status_code, 200)
        self.assertIn('wishes removed successfully', remove_all_response.get_json()['message'])

        get_all_response = self.app.get('/wishes')
        self.assertEqual(len(get_all_response.get_json()), 0)

if __name__ == '__main__':
    unittest.main()

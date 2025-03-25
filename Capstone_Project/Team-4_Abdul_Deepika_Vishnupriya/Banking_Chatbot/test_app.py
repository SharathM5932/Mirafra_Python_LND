import unittest
from app import app  # Assuming your Flask app is in a file called `app.py`
from flask import session
import json

class TestFlaskApp(unittest.TestCase):
    # Setup and teardown for the tests
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test_secret_key'  # Use a test secret key
        self.client = app.test_client()

    def tearDown(self):
        pass

    # Test home page
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to DAV Bank", response.data)  # Check for the word "Welcome to DAV Bank" in the response

    # Test contact page GET
    def test_contact_page_get(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Contact Us", response.data)  # Check for the word "Contact Us"

    # Test contact page POST with valid data
    def test_contact_page_post_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'This is a test message.'
        }
        response = self.client.post('/contact', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Thank you for contacting us!", response.data)  # Check for the success message

    # Test signup page GET
    def test_signup_page_get(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create an Account", response.data)  # Check for the phrase "Create an Account"

    # Test signup with valid data
    def test_signup_valid(self):
        data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'Test@1234',
            'account_number': '1234567'
        }
        response = self.client.post('/signup', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Account created successfully!", response.data)

    # Test signup with invalid data (invalid email)
    def test_signup_invalid_email(self):
        data = {
            'email': 'invalid-email',
            'username': 'testuser',
            'password': 'Test@1234',
            'account_number': '1234567'
        }
        response = self.client.post('/signup', data=data)
        self.assertIn(b"Invalid email format.", response.data)

    # Test login page GET
    def test_login_page_get(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Log In", response.data)

    # Test login with valid credentials
    def test_login_valid(self):
        # First, create a user
        self.test_signup_valid()

        data = {
            'username': 'testuser',
            'password': 'Test@1234'
        }
        response = self.client.post('/login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to your dashboard", response.data)

    # Test login with invalid credentials
    def test_login_invalid(self):
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }
        response = self.client.post('/login', data=data)
        self.assertIn(b"Invalid username or password.", response.data)

    # Test dashboard page (requires login)
    def test_dashboard_without_login(self):
        response = self.client.get('/dashboard', follow_redirects=True)
        self.assertIn(b"Please log in to access the dashboard.", response.data)

    def test_dashboard_with_login(self):
        # Login first
        self.test_login_valid()

        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to your dashboard", response.data)

    # Test chatbot route
    def test_chatbot(self):
        # Login first
        self.test_login_valid()

        data = {
            'message': 'Hello'
        }
        response = self.client.post('/chat', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to DAV Bank!", response.data)  # Ensure chatbot greeting is returned

    def test_chatbot_not_logged_in(self):
        data = {
            'message': 'Hello'
        }
        response = self.client.post('/chat', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"User not logged in", response.data)

    # Test logout
    def test_logout(self):
        # Login first
        self.test_login_valid()

        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"User 'testuser' logged out successfully.", response.data)

    # Test 404 error page
    def test_404_error(self):
        response = self.client.get('/non-existent-page')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Page not found", response.data)



if __name__ == '__main__':
    unittest.main()

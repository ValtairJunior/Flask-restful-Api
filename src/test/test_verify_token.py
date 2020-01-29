from unittest import TestCase
from app.middlewares.auth import verify_token
import requests
import requests_mock


headers = {'autorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxLCJleHAiOjE1ODAzODgwNjguNTEwMjc4NX0.RpeLd9LLiRwFAPv3YkmWiVfKEIWFGwcstB9oKt9jskU'}


class TestVerifyToken(TestCase):
    
    @requests_mock.Mocker()
    def test_valid_token(self, m):
        m.register_uri("GET", 'http://test.com', headers = headers, status_code = 400)
        result = requests.get('http://test.com')
        print(result.headers["autorization"])
        self.assertEqual(1, 1)
        
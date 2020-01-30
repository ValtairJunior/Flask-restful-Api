from unittest import TestCase
from app.middlewares.auth import verify_token, encoded_token
import requests
import requests_mock
import jwt


class TestVerifyToken(TestCase):
    
    @requests_mock.Mocker()
    def test_valid_token(self, m):
        token = encoded_token(1)
        headers = {'autorization': token}
        m.register_uri("GET", 'http://test.com', headers = headers, status_code = 400)
        result = requests.get('http://test.com')
        token = result.headers["autorization"]
        result_id = verify_token(token)['id']
        self.assertEqual( 1,result_id )
    
    @requests_mock.Mocker()
    def test_undefined_token(self, m):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxLCJleHAiOjE1ODAzMjkxMjguOTQ5NDk2fQ.uvZlEPyKY7wIMJz4IagYPKQrs92bH6s2hz0Lyr2blho"
        result = verify_token(token)
        self.assertEqual( "Signature has expired.",result['message'] )
        
    @requests_mock.Mocker()
    def test_invalid_token(self, m):
        token = "J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxLCJleHAiOjE1ODAzMjkxMjguOTQ5NDk2fQ.uvZlEPyKY7wIMJz4IagYPKQrs92bH6s2hz0Lyr2blho"
        result = verify_token(token)
        self.assertEqual( "Invalid Token.",result['message'] )
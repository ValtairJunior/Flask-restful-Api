from flask import current_app, request
from datetime import datetime
from time import time
import jwt 


def encoded_token(id, expires_in=86400):
    return jwt.encode({'auth': id, 'exp': time() + expires_in}, current_app.config['SECRET_KEY'] , algorithm='HS256').decode('utf-8')
    


def decode_token(token):
    result = jwt.decode(token, current_app.config['SECRET_KEY'],
                    algorithms=['HS256'], options={'exp': False})['auth']
    return result

        

def verify_token():
    token = request.headers.get('authorization')
    if token is None:
            return {"message": f"invalid Token is {token}"}
    try:
        verified_token = decode_token(token)
    except jwt.ExpiredSignatureError:
        return {"message":"Signature has expired."}, 401
    except jwt.DecodeError:
        return {"message": "Error decoding signature"}, 401
    except jwt.InvalidTokenError:
        return {"message": "invalid Token"}, 401
    return {"id":verified_token}
    
    
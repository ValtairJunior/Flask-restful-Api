from flask import current_app, request
from instance import config
from datetime import datetime
from time import time
import jwt 


key =  current_app.config['SECRET_KEY'] if (current_app) else "testKey"

def encoded_token(id, expires_in=86400):
    return jwt.encode({'auth': id, 'exp': time() + expires_in}, key  , algorithm='HS256').decode('utf-8')
    


def decode_token(token):
    result = jwt.decode(token, key, algorithms=['HS256'], options={'exp': False})['auth']
    return result

        

def verify_token(token):
    try:
        verified_token = decode_token(token)
    except jwt.ExpiredSignatureError:
        return {"message":"Signature has expired.", "status": 401}
    # except jwt.DecodeError:
    #     return {"message": "Error decoding signature", "status": 401}
    except jwt.InvalidTokenError:
        return {"message": "Invalid Token.", "status": 401}
    return {"id":verified_token}
    
    
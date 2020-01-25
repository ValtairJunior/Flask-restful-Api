from flask import current_app
from datetime import datetime
from time import time
import jwt 



def encoded_token(id, expires_in=600):
    return jwt.encode({'auth': id, 'exp': time() + expires_in},
                      current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    
def decode_token(token):
    id = jwt.decode(token, current_app.config['SECRET_KEY'],
                    algorithms=['HS256'])['auth']
    return id



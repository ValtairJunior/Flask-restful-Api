from flask_restful import Resource
from app.middlewares import encoded_token, decode_token



class  Session(Resource):
    def get(self, auth_id):
        token = encoded_token(auth_id)
        print(decode_token(token))
        return {"Token": token}



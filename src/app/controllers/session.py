from flask_restful import Resource, request

from app.middlewares import encoded_token, decode_token


class  Session(Resource):
    def post(self):
        json_data = request.get_json()
        print(json_data)
        # token = encoded_token(auth_id)
        return 'ok'



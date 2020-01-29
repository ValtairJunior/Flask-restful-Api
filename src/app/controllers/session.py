from flask_restful import Resource, request
from app.middlewares import encoded_token
from app.models.user import check_password, User
from app.middlewares.auth import encoded_token, decode_token

user_model = User()


class  Session(Resource):
    def post(self):
        json_data = request.get_json()
        user = user_model.query.filter_by(email=json_data["email"]).first()
        if not user:
            return {"message": "User not found"}, 401
        if not check_password(password_hash = user.password, password = json_data["password"] ):
            return {"message" : "incorrect password"}, 401
        token = encoded_token(user.id)
        return {"token":token, "name": user.name, "email": user.email}



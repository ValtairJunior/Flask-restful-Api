from flask_restful import Resource, current_app, request
from app.models.user import set_password, User
from app.middlewares.auth import decode_token, verify_token

user_model = User()


class UserController(Resource):
    def post(self):
        json_data = request.get_json()
        user = user_model.query.filter_by(email=json_data["email"]).first()
        if user:
            return {"message": "User email already exists"}, 400
        user_model.name = json_data["name"]
        user_model.email = json_data["email"] 
        user_model.password = set_password(json_data["password"])
        current_app.db.session.add(user_model)
        current_app.db.session.commit()
        return {"message": "User successfully registered"}, 200
    
    def get(self):
        result = verify_token()
        return result

    def put(self):
        pass
    
    def delete(self):
        pass

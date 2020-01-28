from flask_restful import Resource, current_app
from flask import request
from app.middlewares.serializers import UserSchema 
from app.models.user import User

# user_schema = UserSchema()

class User(Resource):
    def post(self):
        json_data = request.get_json()
        data = User(name ='livro', email = 'email', password_hash = 'senha')
        
        # data = user_schema.load(json_data)
        # current_app.db.session.add(data)
        # current_app.db.session.commit()
        
        print(User.query.all())
        return "salvo"
        
    def get():
        pass
    
    def put():
        pass
    
    def delete():
        pass

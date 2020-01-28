from app.middlewares import ma
from app.models.user import User
from app.models.friendship import Friendship
from app.models.message import Message



class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
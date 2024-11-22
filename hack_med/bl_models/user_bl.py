from flask_jwt_extended import create_access_token

from hack_med.dal_models.user_dal import UserDAL
class UserBL:
    @staticmethod
    def create_jwt(user_id):
        token = create_access_token(identity=id)
        return token
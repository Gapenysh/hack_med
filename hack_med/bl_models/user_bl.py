from flask_jwt_extended import create_access_token

from hack_med.dal_models.user_dal import UserDAL
class UserBL:
    @staticmethod
    def create_jwt(user_id):
        token = create_access_token(identity=id)
        return token

    @staticmethod
    def add_feedback(client_id, doctor_id, rating, detail, date):
        success = UserDAL.add_doctor_feedback(client_id, doctor_id, rating, detail, date)
        return success
from hack_med.dal_models.doctor_dal import DoctorDAL
from flask_jwt_extended import create_access_token
class DoctorBL:
    @staticmethod
    def create_jwt(user_id):
        token=create_access_token(identity=id)
        return token

from hack_med.dal_models.doctor_dal import DoctorDAL
from flask_jwt_extended import create_access_token
class DoctorBL:
    @staticmethod
    def create_jwt(user_id):
        token=create_access_token(identity=id)
        return token

    @staticmethod
    def get_all_doctors():

        result = DoctorDAL.get_all_doctors()

        print(result)
        return result

    @staticmethod
    def get_all_doctors_with_duty():
        result = DoctorDAL.get_all_duty_doctors()

        return result

    @staticmethod
    def get_category_doctors():
        result = DoctorDAL.get_all_specialities()
        return result
    @staticmethod
    def get_profile_doctor(doc_id: int):
        doc_info = DoctorDAL.get_info_doctor_by_id(doc_id)
        doc_rating = DoctorDAL.get_avg_rating(doc_id)
        doc_feedbacks = DoctorDAL.get_feedbacks_doctor_by_id(doc_id)
        all_info = {
            "doctor_info": doc_info,
            "avg_rating": round(doc_rating, 1),
            "feedbacks": doc_feedbacks
        }
        return all_info

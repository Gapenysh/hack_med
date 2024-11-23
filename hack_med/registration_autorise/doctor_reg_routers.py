from flask import Blueprint, request, jsonify
from hack_med.bl_models.doctor_bl import DoctorBL
router = Blueprint("registration_doctor_router", __name__)


# @router.route("/registr_doc", methods=["POST"])
# def registr_user():
#     name = request.json.get("name", None)
#     # password = request.json.get("password", None)
#     number = request.json.get("number", None)
#     email = request.json.get("email", None)
#     other_info = request.json.get("info", None)
#     # password = request.json.get("password", None)
#     print(number, email)
#     if number is None or email is None:
#         print("Ошибка получения данных от frontend")
#         return jsonify({"message": "Error with transfering data from frontend (password or number doesn't found)",
#                         "message2": "Пароль или номер не найден"})
#     else:
#         data = DoctorBL.add_new_doctor(number, email)
#         if not data:
#             return jsonify({"message": "This number also registred",
#                             "True?": data})
#         return jsonify({"message": "Life is good!",
#                         "True?": data})


@router.route("/auth_only_doctor", methods=["GET"])
def login_doctor():
    doc_info = DoctorBL.get_info_one_doc()
    return doc_info

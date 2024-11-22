from flask import Blueprint, request, jsonify
from hack_med.bl_models.doctor_bl import DoctorBL
router = Blueprint("registration_doctor_router", __name__)


@router.route("/registr_doc", methods=["POST"])
def registr_user():
    name = request.json.get("name", None)
    # password = request.json.get("password", None)
    number = request.json.get("number", None)
    email = request.json.get("email", None)
    other_info = request.json.get("info", None)
    # password = request.json.get("password", None)
    print(number, email)
    if number is None or email is None:
        print("Ошибка получения данных от frontend")
        return jsonify({"message": "Error with transfering data from frontend (password or number doesn't found)",
                        "message2": "Пароль или номер не найден"})
    else:
        data = DoctorBL.add_new_doctor(number, email)
        if not data:
            return jsonify({"message": "This number also registred",
                            "True?": data})
        return jsonify({"message": "Life is good!",
                        "True?": data})


# @router.route("/auth_doc", methods=["POST"])
# def login():
#     number = request.json.get("phone", None)
#     password = request.json.get("password", None)
#     password = request.json.get("password", None)
#     password = request.json.get("password", None)
#     if number == None or password == None:
#         print("Ошибка получении данных от frontend")
#         return jsonify({"message": "Error with transfering data}")
#
#     else:
#         doc_data = DoctorBL.check_data(number, email)
#         if doc_data != Null:
#             return jsonify({"message": "doctor exist"})
#             if res == True:
#                 access_token = DoctorBL.create_token(doc_data['id'])
#                 print("Авторизация прошла")
#                 return jsonify({"message": "Nice!",
#                                 "jwt-token": access_token,
#                                 "number": number})
#             else:
#                 return jsonify({"message": "Пароли не совпадают"})
#         else:

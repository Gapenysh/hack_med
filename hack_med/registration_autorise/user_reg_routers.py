from flask import Blueprint, request, jsonify
from hack_med.bl_models.user_bl import UserBL

router = Blueprint("registration_user_router", __name__)

# @router.route("/registr", methods=["POST"])
# def registr_user():
#     number = request.json.get("phone", None)
#     password = request.json.get("password", None)
#     password = request.json.get("password", None)
#     password = request.json.get("password", None)
#     password = request.json.get("password", None)
#     print(number, password)
#     if number is None or password is None:
#         print("Ошибка получения данных от frontend")
#         return jsonify({"message": "Error with transfering data from frontend (password or number doesn't found)",
#                         "message2": "Пароль или номер не найден"})
#     else:
#         data = UserBL.add_new_user(number, password)
#         if not data:
#             return jsonify({"message": "This number also registred",
#                             "True?": data})
#         return jsonify({"message": "Life is good!",
#                         "True?": data})

@router.route("/auth_only", methods=["GET"])
def login():
    client_info = UserBL.get_info_by_number()
    return client_info
from flask import Blueprint, request, jsonify

router = Blueprint("registration_user_router", __name__)

@router.route("/registr", methods=["POST"])
def registr_user():
    number = request.json.get("phone", None)
    password = request.json.get("password", None)
    password = request.json.get("password", None)
    password = request.json.get("password", None)
    password = request.json.get("password", None)
    print(number, password)
    if number is None or password is None:
        print("Ошибка получения данных от frontend")
        return jsonify({"message": "Error with transfering data from frontend (password or number doesn't found)",
                        "message2": "Пароль или номер не найден"})
    else:
        data = UserBL.add_new_user(number, password)
        if not data:
            return jsonify({"message": "This number also registred",
                            "True?": data})
        return jsonify({"message": "Life is good!",
                        "True?": data})

@router.route("/auth", methods=["POST"])
def login():
    number = request.json.get("phone", None)
    password = request.json.get("password", None)
    password = request.json.get("password", None)
    password = request.json.get("password", None)
    if number == None or password == None:
        print("Ошибка получении данных от frontend")
        return jsonify({"message": "Error with transfering data from frontend (password or number doesn't found)",
                        "message2": "Пароль или номер не передан"})
    else:
        user_data = UserLogin.refactor_data_to_json_from_number(number)
        if user_data != 401:
            res = check_password_hash(user_data['password'], password)
            if res == True:
                access_token = UserLogin.create_token(user_data['id'])
                print("Авторизация прошла")
                return jsonify({"message": "Nice!",
                                "jwt-token": access_token,
                                "number": number})
            else:
                return jsonify({"message": "Пароли не совпадают"})
        else:
            return jsonify({"message": "Ошибка в получении данных либо номер не зарегистрирован (401)"})
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import settings

from hack_med import med_blueprint

app = Flask(__name__)
app.register_blueprint(med_blueprint)

app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = settings.JWT_TOKEN_LOCATION
jwt = JWTManager(app)

CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=6001)

__all__ = ("registration_autorise_blueprint")

from flask import Blueprint
from doctor_reg_routers import router as doc_reg
from user_reg_routers import router as user_reg


registration_autorise_blueprint = Blueprint("reg_login_roter", __name__)


registration_autorise_blueprint.register_blueprint(user_reg)
registration_autorise_blueprint.register_blueprint(doc_reg)
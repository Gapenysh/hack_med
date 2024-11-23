__all__ = ("doctors_blueprint")

from flask import Blueprint
from .doctor_routes import router as doc_router
# from .user_reg_routers import router as user_reg


doctors_blueprint = Blueprint("reg_login_roter", __name__)


# doctors_blueprint.register_blueprint(user_reg)
doctors_blueprint.register_blueprint(doc_router)
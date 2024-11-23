__all__ = ("feedback_blueprint")

from flask import Blueprint
from .feedback_routes import router as feedback_router
# from .user_reg_routers import router as user_reg


feedback_blueprint = Blueprint("feed_roter", __name__)


# doctors_blueprint.register_blueprint(user_reg)
feedback_blueprint.register_blueprint(feedback_router)
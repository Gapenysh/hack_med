__all__ = ("med_blueprint",)
#
from flask import Blueprint

from hack_med.registration_autorise import registration_autorise_blueprint
#
# from .analysis import analysis_blueprint
# from .doctors import doctors_blueprint
# from .records import records_blueprint
# from .admin import admin_blueprint
# from .services import services_blueprint
#
med_blueprint = Blueprint("med_hack", __name__)
med_blueprint.register_blueprint(registration_autorise_blueprint)
# clinic_blueprint.register_blueprint(analysis_blueprint)
# clinic_blueprint.register_blueprint(doctors_blueprint)
# clinic_blueprint.register_blueprint(records_blueprint)
# clinic_blueprint.register_blueprint(services_blueprint)
# clinic_blueprint.register_blueprint(admin_blueprint)
#

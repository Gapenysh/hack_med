
from flask import Blueprint, request, jsonify
from hack_med.bl_models.user_bl import UserBL

router = Blueprint("doctor_router", __name__)

# @router.route("/request", methods=["GET"])
# def all_requests():
#     requests =
# @router.route("/request", methods=["POST"])

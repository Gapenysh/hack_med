from flask import Blueprint, request, jsonify
from hack_med.bl_models.user_bl import UserBL
router = Blueprint("client_router", __name__)

@router.route("/profile/<int:id>", methods=["GET"])
def get_profile_by_id(id):
    pass

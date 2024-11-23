from flask import Blueprint, request, jsonify
from hack_med.bl_models.user_bl import UserBL
router = Blueprint("feedback_router", __name__)


@router.route("/feedback", methods=["POST"])
def add_feedback():
    client_id = request.json.get("client_id", None)
    doctor_id = request.json.get("doctor_id", None)
    rating = request.json.get("rating", None)
    detail = request.json.get("detail", None)
    date = request.json.get("date", None)

    success = UserBL.add_feedback(client_id, doctor_id, rating, detail, date)

    if success:
        return jsonify({"message": "Feedback added successfully"}), 200
    else:
        return jsonify({"message": "Failed to add feedback"}), 400
from flask import Blueprint, request, jsonify
from hack_med.bl_models.doctor_bl import DoctorBL
router = Blueprint("doctor_router", __name__)


@router.route("/doctors", methods=["GET"])
def get_all_doctors():
    doctors = DoctorBL.get_all_doctors()
    return doctors

@router.route("/doctors_duty", methods=["GET"])
def get_all_doctors_duty():
    doctors = DoctorBL.get_all_doctors_with_duty()
    return doctors

@router.route("/get_categories", methods=["GET"])
def get_all_categories():
    doctors = DoctorBL.get_category_doctors()
    return doctors

@router.route("/doctors/<int:id>", methods=["GET"])
def get_info_doc_by_id(id):
    info = DoctorBL.get_profile_doctor(id)
    return info
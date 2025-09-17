from flask import Blueprint, request, jsonify
from models import db, Booking

booking_bp = Blueprint("bookings", __name__)

@booking_bp.route("/", methods=["POST"])
def create_booking():
    data = request.json
    new_booking = Booking(
        customer_name=data["customer_name"],
        email=data["email"],
        phone=data.get("phone"),
        package_id=data["package_id"],
        checkin_date=data.get("checkin_date"),
        checkout_date=data.get("checkout_date")
    )
    db.session.add(new_booking)
    db.session.commit()
    return jsonify({"message": "Booking created successfully!"}), 201

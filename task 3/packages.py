from flask import Blueprint, request, jsonify
from models import db, Package

package_bp = Blueprint("packages", __name__)

@package_bp.route("/", methods=["GET"])
def get_packages():
    packages = Package.query.all()
    return jsonify([{
        "id": p.id,
        "title": p.title,
        "description": p.description,
        "price": p.price,
        "duration": p.duration,
        "pax": p.pax
    } for p in packages])

@package_bp.route("/", methods=["POST"])
def add_package():
    data = request.json
    new_package = Package(
        title=data["title"],
        description=data["description"],
        price=data["price"],
        duration=data["duration"],
        pax=data["pax"],
        destination_id=data["destination_id"]
    )
    db.session.add(new_package)
    db.session.commit()
    return jsonify({"message": "Package added successfully!"}), 201

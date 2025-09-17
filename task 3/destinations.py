from flask import Blueprint, jsonify
from models import Destination

destination_bp = Blueprint("destinations", __name__)

@destination_bp.route("/", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([{
        "id": d.id,
        "name": d.name,
        "country": d.country,
        "description": d.description,
        "rating": d.rating
    } for d in destinations])

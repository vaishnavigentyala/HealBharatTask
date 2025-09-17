from flask import Blueprint, jsonify
from models import Gallery

gallery_bp = Blueprint("gallery", __name__)

@gallery_bp.route("/", methods=["GET"])
def get_gallery():
    images = Gallery.query.all()
    return jsonify([{
        "id": g.id,
        "image_url": g.image_url,
        "caption": g.caption
    } for g in images])

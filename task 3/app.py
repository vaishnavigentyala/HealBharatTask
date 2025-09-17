from flask import Flask
from flask_cors import CORS
from extensions import db   # ✅ import db from extensions

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # ✅ initialize db

    # Register Blueprints
    from routes.destinations import destination_bp
    from routes.packages import package_bp
    from routes.bookings import booking_bp
    from routes.gallery import gallery_bp

    app.register_blueprint(destination_bp, url_prefix="/api/destinations")
    app.register_blueprint(package_bp, url_prefix="/api/packages")
    app.register_blueprint(booking_bp, url_prefix="/api/bookings")
    app.register_blueprint(gallery_bp, url_prefix="/api/gallery")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # ✅ Create tables
    app.run(debug=True)

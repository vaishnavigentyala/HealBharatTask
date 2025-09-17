from extensions import db  # ✅ import db here

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, default=4.5)

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    pax = db.Column(db.Integer, nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'))
    checkin_date = db.Column(db.String(20))
    checkout_date = db.Column(db.String(20))

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(255), nullable=True)

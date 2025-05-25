from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///period_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_group = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    floor = db.Column(db.String(50), nullable=True)
    pads_availability = db.Column(db.String(10), default='Low')
    tampons_availability = db.Column(db.String(10), default='Low')
    free = db.Column(db.Boolean, nullable=False)
    accessibility = db.Column(db.Boolean, nullable=True)
    last_updated = db.Column(db.DateTime, default=datetime.now(timezone.utc))


with app.app_context():
    db.create_all()

@app.route('/') #READ
def home():
    locations = Location.query.all()
    grouped_locations = {}
    for loc in locations:
        if loc.location_group not in grouped_locations:
            grouped_locations[loc.location_group] = []
            grouped_locations[loc.location_group].append(loc)

    return render_template('home.html', locations=locations)

@app.route('/update_stock/<int:location_id>', methods=['POST']) #UPDATE
def update_stock(location_id):
    data = request.json
    location = Location.query.get_or_404(location_id)

    location.pads_availability = data['pads_availability']
    location.tampons_availability = data['tampons_availability']
    location.last_updated = datetime.now(timezone.utc)

    db.session.commit()
    return jsonify({"success": True})


@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/locations')
def locations():
    all_locations = Location.query.all()
    locations_data = [{
        'id': loc.id,
        'location_group' : loc.location_group,
        'name': loc.name,
        'latitude': loc.latitude,
        'longitude': loc.longitude,
        'floor' : loc.floor,
        'pads_availability': getattr(loc, 'pads_availability', 'N/A'),
        'tampons_availability': getattr(loc, 'tampons_availability', 'N/A'),
        'free' : loc.free,
        'accessibility': loc.accessibility,
        'last_updated': loc.last_updated.strftime('%Y-%m-%d %H:%M:%S') if loc.last_updated else ''
    } for loc in all_locations]
    
    return jsonify(locations_data)


if __name__ == '__main__':
    app.run(debug=True)
from app import app, db, Location
from datetime import datetime, timezone

with app.app_context():
    new_location = Location(
        name="Aldrich Hall - basement",
        latitude=33.64841625857725,
        longitude=-117.84122708476183,
        pads_availability="Stocked",    
        tampons_availability="Stocked",
        free=True,
        accessibility=True,
        last_updated=datetime.now(timezone.utc)
    )

    db.session.add(new_location)
    db.session.commit()

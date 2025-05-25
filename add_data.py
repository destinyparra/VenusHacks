from app import app, db, Location
from datetime import datetime, timezone
import random

locations_raw = [
    {"name": "Aldrich Hall - Basement", "latitude": 33.64841625857725, "longitude": -117.84122708476183},
    {"name": "Aldrich Hall - 2nd floor, 214", "latitude": 33.64841625857725, "longitude": -117.84122708476183},
    {"name": "Aldrich Hall - 2nd floor, 216", "latitude": 33.64841625857725, "longitude": -117.84122708476183},
    {"name": "Aldrich Hall - 6th floor, 601", "latitude": 33.64841625857725, "longitude": -117.84122708476183},
    {"name": "Aldrich Hall - 6th floor, 604", "latitude": 33.64841625857725, "longitude": -117.84122708476183},
    {"name": "Anteater Learning Pavilion - 1st Floor", "latitude": 33.647189306833425, "longitude": -117.84462947326799},
    {"name": "Anteater Learning Pavilion - 2nd Floor", "latitude": 33.647189306833425, "longitude": -117.84462947326799},
    {"name": "Anteater Learning Pavilion - 3rd Floor", "latitude": 33.647189306833425, "longitude": -117.84462947326799},
    {"name": "Biological Sciences III - Basement", "latitude": 33.64552858342245, "longitude": -117.84571966652165},
    {"name": "Biological Sciences III - Level 1", "latitude": 33.64552858342245, "longitude": -117.84571966652165},
    {"name": "Anteater Recreation Center - 1st floor, 104", "latitude": 33.643655696764164, "longitude": -117.82791864570751},
    {"name": "Anteater Recreation Center - 1st floor, 105", "latitude": 33.643655696764164, "longitude": -117.82791864570751},
    {"name": "Anteater Recreation Center - 2nd floor, 272", "latitude": 33.643655696764164, "longitude": -117.82791864570751},
    {"name": "Anteater Recreation Center - 2nd Floor, 275", "latitude": 33.643655696764164, "longitude": -117.82791864570751},
]

availability_options = ["Low", "Medium", "Stocked"]

def extract_floor(name):
    parts = name.split(" - ")
    if len(parts) > 1:
        return parts[1]
    return None

def assign_location_group(name):
    return name.split(" - ")[0]

with app.app_context():
    db.drop_all()
    db.create_all()

    for loc in locations_raw:
        location = Location(
            name=loc["name"],
            latitude=loc["latitude"],
            longitude=loc["longitude"],
            floor=extract_floor(loc["name"]),
            location_group=assign_location_group(loc["name"]),
            pads_availability=random.choice(availability_options),
            tampons_availability=random.choice(availability_options),
            free=random.choice([True, False]),
            accessibility=random.choice([True, False]),
            last_updated=datetime.now(timezone.utc)
        )
        db.session.add(location)

    db.session.commit()
    print(f"Inserted {len(locations_raw)} new locations with auto-incremented IDs.")

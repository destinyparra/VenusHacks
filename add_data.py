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
    {"name": "Rowland Hall - Basement B92", "latitude": 33.64436053124253, "longitude": -117.84418961309437},
    {"name": "Rowland Hall - Basement B94", "latitude": 33.64436053124253, "longitude": -117.84418961309437},
    {"name": "McGaugh Hall - Basement B225", "latitude": 33.64537096799353, "longitude": -117.8447793333362},
    {"name": "Student Center - Level 2 G213", "latitude": 33.64918088503983, "longitude": -117.84215013097759},
    {"name": "Student Center - Level 2 G215", "latitude": 33.64918088503983, "longitude": -117.84215013097759},
    {"name": "Student Center - Level 3 G319", "latitude": 33.64918088503983, "longitude": -117.84215013097759},
    {"name": "Engineering Tower - Level 1, Room 125", "latitude": 33.645069413565146, "longitude": -117.84102733097895},
    {"name": "Humanities Hall - Level 1, Room 120", "latitude": 33.64749070041358, "longitude": -117.84409780634692},
    {"name": "Science Library - Level 2, Room 270", "latitude": 33.64603186827473, "longitude": -117.84663301309423},
    {"name": "Science Library - Level 5, Room 582", "latitude": 33.64603186827473, "longitude": -117.84663301309423},
    {"name": "Starbucks @ Student Center - Room 1", "latitude": 33.64830457008609, "longitude": -117.84200620341088},
    {"name": "Social Science Lab - Level 2, Room 249", "latitude": 33.64605951593628, "longitude": -117.84019493467021},
    {"name": "Social Science Lab - Level 2, Room 250", "latitude": 33.64605951593628, "longitude": -117.84019493467021},
    {"name": "Information & Computer Science - Level 2, Room 239", "latitude": 33.644721763710194, "longitude": -117.84177974008364},
    {"name": "Information & Computer Science - Level 2, Room 267", "latitude": 33.644721763710194, "longitude": -117.84177974008364},
    {"name": "Information & Computer Science - Level 4, Room 430", "latitude": 33.644721763710194, "longitude": -117.84177974008364},
    {"name": "Information & Computer Sciences II - Level 2, Room 222", "latitude": 33.644130641041926, "longitude": -117.84181660779763},
    {"name": "Information & Computer Sciences II - Level 2, Room 224", "latitude": 33.644130641041926, "longitude": -117.84181660779763},
    {"name": "Information & Computer Sciences II - Level 2, Room 228", "latitude": 33.644130641041926, "longitude": -117.84181660779763},
    {"name": "Information & Computer Sciences II - Level 2, Room 230", "latitude": 33.644130641041926, "longitude": -117.84181660779763},
    {"name": "Berk Hall", "latitude": 33.6464010731517, "longitude": -117.84945452909629},
    {"name": "Cross Cultural Center", "latitude": 33.64796140694652, "longitude": -117.84183937327744},
    {"name": "Croul Hall", "latitude": 33.64386465195876, "longitude": -117.84468073095017},
    {"name": "Gateway Study Center", "latitude": 33.64756405097313, "longitude": -117.84165041560507},
    {"name": "Gavin Herbert Eye Institute", "latitude": 33.641875719575665, "longitude": -117.85219551560516},
    {"name": "Hewitt Hall", "latitude": 33.64349284800469, "longitude": -117.8518024021139},
    {"name": "Krieger Hall", "latitude": 33.647942608266554, "longitude": -117.84354618862262},
    {"name": "Medical Education Bldg.", "latitude": 33.644796250218846, "longitude": -117.85218980211381},
    {"name": "Medical Sciences C", "latitude": 33.64579592694056, "longitude": -117.8505027597864},
    {"name": "Medical Surge II", "latitude": 33.64714200286829, "longitude": -117.85042987698527},
    {"name": "Music & Media Building", "latitude": 33.64950783420398, "longitude": -117.84447327667768},
    {"name": "Rockwell Engr. Center", "latitude": 33.64405762471028, "longitude": -117.84059998862271},
    {"name": "Schneiderman Lecture Hall", "latitude": 33.645798537622944, "longitude": -117.8447573039678},
    {"name": "Social & Behavioral Sciences Gateway", "latitude": 33.64758536453718, "longitude": -117.83906630211386},
    {"name": "Social Science Plaza B", "latitude": 33.6472138340985, "longitude": -117.83912613095008},
    {"name": "Steinhaus Hall", "latitude": 33.64641757311412, "longitude": -117.84489568862256},
    {"name": "Humanities Gateway", "latitude": 33.648251992362475, "longitude": -117.84443361129894},
    {"name": "Langson Library", "latitude": 33.647368202328465, "longitude": -117.84111867327755},
    {"name": "Social Science Tower", "latitude": 33.646779818239835, "longitude": -117.8401352886227},
    {"name": "Social Science Hall", "latitude": 33.64639657871138, "longitude": -117.83999462909637},
    {"name": "Donald Bren Hall", "latitude": 33.64343371634265, "longitude": -117.84205141745889},
    {"name": "Interdisciplinary Science and Engineering Building", "latitude": 33.64319646016414, "longitude": -117.84374780994303},
    {"name": "Reines Hall", "latitude": 33.64427937024997, "longitude": -117.84348467199575},
    {"name": "The Paul Merage School of Business", "latitude": 33.64707143378149, "longitude": -117.837820282872},
    {"name": "Pippin Commons", "latitude": 33.64504821560184, "longitude": -117.83682715356913},
    {"name": "Anteater Instruction and Research Building", "latitude": 33.643012823108286, "longitude": -117.83774859178519},
    {"name": "Engineering Gateway", "latitude": 33.64317699962084, "longitude": -117.83960162596028},
    {"name": "The Anteatery", "latitude": 33.6511269878, "longitude": -117.84575379603787},
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

from sky_ride_db import SkyRideDB
from client.client import Client
from icecream import ic


sky_db = SkyRideDB()
sky_db.create_table(
    "", 
    "clients", 
    "clients",
    sky_db.collect_column_names_and_types(Client().column_titles_table())
    )
for _ in range(5):
    sky_db.add_object_table(
        "",
        "clients",
        "clients",
        sky_db.get_column_names("", "clients", "clients"),
        Client().customer_data()
        )
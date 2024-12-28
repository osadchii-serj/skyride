from data.db import SkyRideDatabase
from data.fake_values import FakeValues

if __name__ == "__main__":
    f_values = FakeValues()

    clients_db = SkyRideDatabase(
        path_name_database="clients/clients.db",
        table_name="clients",
        column_name="""
        customer_id INTEGER PRIMARY KEY,
        avatar BLOB,
        name TEXT,
        middle_name TEXT,
        surname TEXT,
        age INTEGER,
        email TEXT,
        phone TEXT,
        password TEXT,
        gender TEXT,
        address TEXT,
        city TEXT,
        postal_code TEXT,
        country TEXT,
        data TEXT
        """
    )
    clients_db.create_database()

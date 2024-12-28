import sqlite3 as sq
from dataclasses import dataclass
from icecream import ic


@dataclass
class SkyRideDatabase:
    path_name_database: str
    table_name: str
    column_name: str

    def create_database(self):
        try:
            connection = sq.connect(self.path_name_database)
            cursor = connection.cursor()
            cursor.execute(
                f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}
            ({self.column_name})
            """
            )
            connection.commit()
        except:
            ic(f"Ошибка создания базы {self.table_name}")
        finally:
            connection.close()


if __name__ == "__main__":
    sdb = SkyRideDatabase(
        path_name_database="clients/clients.db",
        table_name="sky_clients",
        column_name="""
        name TEXT,
        age INTEGER, 
        last_name TEXT
        """,
        column_value="")

    sdb.create_database()

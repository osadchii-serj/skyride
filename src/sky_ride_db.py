from dataclasses import dataclass
from icecream import ic
import sqlite3 as sq


@dataclass
class SkyRideDB:

    def create_table(self, path_file_db: str, name_file_db: str, name_table: str, fields: str):
        try:
            connection = sq.connect(f"{path_file_db}{name_file_db}.db")
            cursor = connection.cursor()
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {name_table} ({fields});
            """
            cursor.execute(create_table_query)
        except sq.Error as error:
            ic(error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def collect_column_names_and_types(self, fields_types: dict):
        fields = ""
        for field, types in fields_types.items():
            fields += f"{field} {types},"
        return fields.rstrip(",")

    def get_column_names(self, path_file_db: str, name_file_db: str, name_table: str):
        try:
            connection = sq.connect(f"{path_file_db}{name_file_db}.db")
            cursor = connection.cursor()
            create_table_query = f"""
            PRAGMA table_info({name_table});
            """
            cursor.execute(create_table_query)
            column_names = [column[1] for column in cursor.fetchall()]
            return tuple(column_names)
        except sq.Error as error:
            ic(error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def add_object_table(self, path_file_db: str, name_file_db: str, name_table: str, fields: str, values: dict):
        columns = ""
        rows = ""
        for column in fields:
            columns += f"{column},"
            rows += f":{column},"
        col = columns.rstrip(",")
        row = rows.rstrip(",")
        try:
            connection = sq.connect(f"{path_file_db}{name_file_db}.db")
            cursor = connection.cursor()
            create_table_query = f"""
            INSERT INTO {name_table} ({col}) VALUES ({row});
            """
            cursor.execute(create_table_query, values)
        except sq.Error as error:
            ic(error)
        finally:
            if connection:
                connection.commit()
                cursor.close()
                connection.close()


if __name__ == "__main__":
    sky_db = SkyRideDB()
    sky_db.create_table("", "clients", "clients", "user_id INTEGER")

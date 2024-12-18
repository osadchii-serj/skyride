import sqlite3 as sq
from faker import Faker
from dataclasses import dataclass
from icecream import ic


@dataclass
class Client:
    faker = Faker("ru_RU")
    table_fields = {
        "clients":
            """
                client_id INTEGER PRIMARY KEY,
                profile_picture BLOB,
                first_name TEXT,
                last_name TEXT,
                email TEXT UNIQUE,
                phone_number TEXT,
                password_hash TEXT,
                gender TEXT,
                address TEXT,
                city TEXT,
                postal_code TEXT,
                country TEXT
            """,
        "payment":
            """
                payment_id INTEGER PRIMARY KEY,
                client_id INTEGER,
                card_number TEXT
            """,
        "history":
            """
                review_id INTEGER PRIMARY KEY,
                client_id INTEGER,
                driver_id INTEGER,
                start_location TEXT,
                end_location TEXT,
                ride_date_time DATETIME,
                status TEXT,
                fare_amount DECIMAL(10, 2)
            """,
        "reviews":
            """
                review_id INTEGER PRIMARY KEY,
                client_id INTEGER,
                driver_id INTEGER,
                rating INTEGER,
                comment TEXT,
                review_date_time DATETIME
            """
    }
    path_db = "clients/"

    def connection_db(self):
        ic()
        for db_name, fields in self.table_fields.items():
            try:
                connection = sq.connect(f"{self.path_db}{db_name}.db")
                cursor = connection.cursor()
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {db_name}
                    (
                        {fields}
                    )
                    """
                )
                ic(f"Создана БД {self.path_db}{db_name}")
            except:
                ic("Ошибка подключения к базе")
            finally:
                connection.close()

    def deleting_table(self, name_table):
        try:
            connection = sq.connect(f"{self.path_db}{name_table}.db")
            cursor = connection.cursor()
            cursor.execute(
                f"""
                DROP TABLE IF EXISTS {name_table}
                """
            )
            ic(f"Таблица {name_table} удалена")
        except:
            ic(f"Ошибка удаления таблицы {name_table}")
        finally:
            connection.close()

    def add_data(self):
        pass

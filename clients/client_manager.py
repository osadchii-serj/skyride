import sqlite3 as sq
from faker import Faker
from dataclasses import dataclass


@dataclass
class Client:
    faker = Faker("ru_RU")
    data_db = {
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
        for db_name, fields in self.data_db.items():
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
                print(f"Создана БД {self.path_db}{db_name}")
            except:
                print("Ошибка подключения к базе")
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
            print(f"Таблица {name_table} удалена")
        except:
            print(f"Ошибка удаления таблицы {name_table}")
        finally:
            connection.close()

    def add_data(self):
        pass

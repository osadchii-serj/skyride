from dataclasses import dataclass
from icecream import ic
from faker import Faker
import random


@dataclass
class Client:

    def column_titles_table(self):
        titles = {
            # "client_id": "INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1",
            "email": "TEXT NOT NULL DEFAULT ''",
            "phone": "TEXT NOT NULL DEFAULT ''",
            "login": "TEXT NOT NULL DEFAULT ''",
            "password": "TEXT NOT NULL DEFAULT ''",
            "first_name": "TEXT NOT NULL DEFAULT ''",
            "patronymic": "TEXT NOT NULL DEFAULT ''",
            "last_name": "TEXT NOT NULL DEFAULT ''",
            "gender": "TEXT NOT NULL DEFAULT ''",
            "age": "INTEGER NOT NULL DEFAULT 0",
            "address": "TEXT NOT NULL DEFAULT ''",
            "city": "TEXT NOT NULL DEFAULT ''",
            "country": "TEXT NOT NULL DEFAULT ''",
            "starting_point": "TEXT NOT NULL DEFAULT ''",
            "final_point": "TEXT NOT NULL DEFAULT ''",
            "date_taxi_order": "TEXT NOT NULL DEFAULT ''",
            "comment": "TEXT NOT NULL DEFAULT ''",
            "rating": "INTEGER NOT NULL DEFAULT 0",
        }
        return titles

    def customer_data(self):
        fake = Faker("ru_RU")

        def create_gender_fio():
            gender = random.choice(['муж', 'жен'])
            if gender == "муж":
                return fake.name_male().split(), gender
            else:
                return fake.name_female().split(), gender
            
        fio, gender = create_gender_fio()
        
        rows = {
            # "client_id": 0,
            "email": fake.email(),
            "phone": fake.phone_number(),
            "login": fake.user_name(),
            "password": fake.password(),
            "first_name": fio[0],
            "patronymic": fio[1],
            "last_name": fio[2],
            "gender": gender,
            "age": fake.random_int(min=10, max=150),
            "address": fake.street_address(),
            "city": fake.city(),
            "country": fake.country(),
            "starting_point": fake.street_address(),
            "final_point": fake.street_address(),
            "date_taxi_order": fake.date_time_between().strftime("%Y-%m-%d %H:%M:%S"),
            "comment": fake.sentence(),
            "rating": fake.random_int(min=1, max=5),
        }
        return rows

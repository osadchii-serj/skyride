from dataclasses import dataclass
from faker import Faker
from PIL import Image
from io import BytesIO
import requests
from icecream import ic
import random


@dataclass
class FakeValues:
    faker = Faker("ru_RU")
    fio = None
    gender = random.choice(["муж", "жен"])
    if gender == "муж":
        fio = faker.name_male().split()
    else:
        fio = faker.name_female().split()

    field_values = {
        "id": faker.uuid4(),
        "image": faker.image_url(width=100, height=100),
        "name": fio[1],
        "middle_name": fio[2],
        "surname": fio[0],
        "email": faker.email(),
        "phone": faker.phone_number(),
        "password": faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "gender": gender,
        "address": faker.street_address(),
        "city": faker.city(),
        "postal_code": faker.postcode(),
        "country": faker.country(),
        "card_number": faker.credit_card_number(),
        "provider": faker.credit_card_provider(),
        "data": faker.date(),
        "status": random.choice(["Завершена", "Отменена", "В пути"]),
        "fare_amount": faker.random_int(min=20, max=300)
    }


if __name__ == "__main__":
    data = FakeValues()
    ic(
        data.field_values["id"],
        data.field_values["image"],
        data.field_values["name"],
        data.field_values["middle_name"],
        data.field_values["surname"],
        data.field_values["email"],
        data.field_values["phone"],
        data.field_values["password"],
        data.field_values["gender"],
        data.field_values["address"],
        data.field_values["city"],
        data.field_values["postal_code"],
        data.field_values["country"],
        data.field_values["card_number"],
        data.field_values["provider"],
        data.field_values["data"],
        data.field_values["status"],
        data.field_values["fare_amount"],
    )

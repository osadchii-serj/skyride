from faker import Faker
import random
from icecream import ic

fake = Faker("ru_RU")


class ClientMeta(type):
    def create_gender():
        fio = None
        gender = random.choice(['муж', 'жен'])
        if gender == "муж":
            fio = fake.name_male().split()
        else:
            fio = fake.name_female().split()
        return fio, gender

    def __new__(cls, name, base, attrs):
        fio, gender = cls.create_gender()
        attrs.update(
            {
                "email": fake.email(),
                "phone": fake.phone_number(),
                "login": fake.user_name(),
                "password": fake.password(),
                "first_name": fio[0],
                "patronymic": fio[1],
                "last_name": fio[2],
                "age": fake.random_int(min=10, max=150),
                "gender": gender,
                "address": fake.street_address(),
                "city": fake.city(),
                "country": fake.country(),
                "starting_point": fake.address(),
                "final_point": fake.address(),
                "date_taxi_order": fake.date_time_between().strftime("%Y-%m-%d %H:%M:%S"),
                "comment": fake.sentence(),
                "rating": fake.random_int(min=1, max=5),
            }
        )
        return type.__new__(cls, name, base, attrs)


if __name__ == "__main__":
    class TestMeta(metaclass=ClientMeta):
        pass

    tm = TestMeta
    ic(tm.__dict__)

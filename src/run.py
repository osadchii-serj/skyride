from client.client import SkyRiderClient
from payment.payment import GlobalFinanceBank
from faker import Faker
from icecream import ic
import random

fake = Faker("ru_RU")


def create_gender():
    fio = None
    gender = random.choice(['муж', 'жен'])
    if gender == "муж":
        fio = fake.name_male().split()
    else:
        fio = fake.name_female().split()
    return fio, gender


user_1 = SkyRiderClient(GlobalFinanceBank())
user_1.registration(
    fake.phone_number(),
    fake.email(),
    fake.user_name(),
    fake.password()
)


fio, gender = create_gender()

user_1.set_bio(
    fio[0],
    fio[1],
    fio[2],
    fake.random_int(min=10, max=150),
    gender
)


user_1.set_address(
    fake.street_address(),
    fake.city(),
    fake.country()
)

user_1.order_taxi(
    fake.address(),
    fake.address(),
    fake.date_time_between().strftime("%Y-%m-%d %H:%M:%S")

)

user_1.payment.registration(
    user_1.first_name,
    user_1.patronymic,
    user_1.last_name,
)

user_1.payment.create_bank_card(
    fake.credit_card_number(),
    fake.credit_card_expire(),
    fake.credit_card_security_code(),
    fake.credit_card_provider()
)

user_1.payment.transfer_money(
    fake.random_int(min=-1000, max=10000)
)

ic(
    user_1.phone,
    user_1.email,
    user_1.login,
    user_1.password,
    user_1.first_name,
    user_1.patronymic,
    user_1.last_name,
    user_1.age,
    user_1.gender,
    user_1.address,
    user_1.city,
    user_1.country,
    user_1.starting_point,
    user_1.final_point,
    user_1.date_taxi_order,
)

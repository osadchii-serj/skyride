from faker import Faker
import random
from icecream import ic
from dataclasses import dataclass

fake = Faker("ru_RU")


class PaymentMeta(type):
    def __new__(cls, name, base, attrs):
        attrs.update(
            {
                "card_number": fake.credit_card_number(),
                "expiry": fake.credit_card_expire(),
                "cvv": fake.credit_card_security_code(),
                "provider": fake.credit_card_provider(),
                "balance": fake.random_int(min=-5000, max=10000),
            }
        )
        return type.__new__(cls, name, base, attrs)


if __name__ == "__main__":
    @dataclass
    class TestPayment(metaclass=PaymentMeta):
        first_name: str
        patronymic: str
        last_name: str

    pm = TestPayment("Иван", "Васильевич", "Борода")
    ic(
        pm.__dict__,
        pm.card_number,
        pm.expiry,
        pm.cvv,
        pm.provider,
        pm.balance,
    )

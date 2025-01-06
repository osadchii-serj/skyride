from icecream import ic
from dataclasses import dataclass
from .payment_meta import PaymentMeta


@dataclass
class GlobalFinanceBank(metaclass=PaymentMeta):
    first_name: str
    patronymic: str
    last_name: str

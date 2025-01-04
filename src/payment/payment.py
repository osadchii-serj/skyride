if __name__ == "__main__":
    from interfaces import Payment
else:
    from .interfaces import Payment
    
from icecream import ic
from dataclasses import dataclass


@dataclass
class GlobalFinanceBank(Payment):
    first_name = None
    patronymic = None
    last_name = None
    card_number = None
    expiry = None
    cvv = None
    security_code = None
    provider = None
    balance = 0

    def registration(self, first_name: str, patronymic: str, last_name: str):
        """Регистрация клиента

        Args:
            first_name (str): имя
            patronymic (str): отчество
            last_name (str): фамилия
        """
        ic()
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        ic(
            f"Банк: {self.__class__.__name__}",
            f"Пользователь: {self.first_name} {
                self.patronymic} {self.last_name}",
        )

    def create_bank_card(self, credit_card_number: str, credit_card_expire: str, credit_card_security_code: str, credit_card_provider: str):
        """Создать карту

        Args:
            credit_card_number (str): номер
            credit_card_expire (str): срок годности
            credit_card_security_code (str): код
            credit_card_provider (str): провайдер
        """
        ic()
        self.card_number = credit_card_number
        self.expiry = credit_card_expire
        self.cvv = credit_card_security_code
        self.provider = credit_card_provider
        ic(
            "Карта создана",
            self.card_number,
            self.expiry,
            self.cvv,
            self.provider
        )

    def transfer_money(self, amount: int):
        ic()
        self.balance = amount
        ic(
            f"Перевод средств {amount}",
            self.balance
        )



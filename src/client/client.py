if __name__ == "__main__":
    from interfaces import Client
else:
    from .interfaces import Client
    
from icecream import ic
from dataclasses import dataclass

@dataclass
class SkyRiderClient(Client):
    payment: str
    email = None
    phone = None
    login = None
    password = None
    first_name = None
    patronymic = None
    last_name = None
    age = None
    gender = None
    address = None
    city = None
    country = None
    starting_point = None
    final_point = None
    date_taxi_order = None
    comment = None
    rating = None

    def registration(self, phone=None, email=None, login=None, password=None):
        """Регистрация пользователя

        Args:
            phone (_str_, optional): _description_. Defaults to None.
            email (_str_, optional): _description_. Defaults to None.
            login (_str_, optional): _description_. Defaults to None.
            password (_str_, optional): _description_. Defaults to None.
        """
        ic()
        if phone and email and login and password:
            self.phone = phone
            self.email = email
            self.login = login
            self.password = password
            ic(f"Пользователь: {self.login} зарегистрирован")
        else:
            ic("Ошибка регистрации")
            

    def set_bio(self, first_name: str, patronymic: str, last_name: str, age: int, gender: str):
        """Добавить биографию

        Args:
            first_name (str): имя
            patronymic (str): отчество
            last_name (str): фамилия
            age (int): возраст
            gender (str): пол
        """
        ic()
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.age = age
        self.gender = gender
        ic(
            self.first_name,
            self.patronymic,
            self.last_name,
            self.age,
            self.gender,
            "Данные биографии добавлены"
        )

    def set_address(self, address: str, city: str, country: str):
        """Добавить адрес

        Args:
            address (str): уличный адрес
            city (str): город
            country (str): страна
        """
        ic()
        self.address = address
        self.city = city
        self.country = country
        ic(
            "Адрес добавлен",
            self.address,
            self.city,
            self.country
        )

    def order_taxi(self, start_point: str, final_point: str, data: str):
        """Заказать такси

        Args:
            start_point (str): стартовая точка
            final_point (str): финальная точка
            data (str): дата
        """
        ic()
        self.starting_point = start_point
        self.final_point = final_point
        self.date_taxi_order = data
        ic(
            "Заказ такси:",
            f"Стартовая точка: {self.starting_point}",
            f"Финальная точка: {self.final_point}",
            f"Дата: {self.date_taxi_order}"
        )

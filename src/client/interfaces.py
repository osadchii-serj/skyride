from abc import ABC, abstractmethod


class Client(ABC):

    @abstractmethod
    def registration(self, phone: str = None, email: str = None, login: str = None, password: str = None):
        raise NotImplementedError

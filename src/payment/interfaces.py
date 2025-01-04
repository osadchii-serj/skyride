from abc import (
    ABC,
    abstractmethod,
)


class Payment(ABC):

    @abstractmethod
    def registration(self):
        raise NotImplementedError

    @abstractmethod
    def transfer_money(self):
        raise NotImplementedError

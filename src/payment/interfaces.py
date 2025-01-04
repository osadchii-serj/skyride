from abc import (
    ABC,
    abstractmethod,
)


class Payment(ABC):

    @abstractmethod
    def registration_user_bank(self):
        raise NotImplementedError

    @abstractmethod
    def transfer_money(self):
        raise NotImplementedError

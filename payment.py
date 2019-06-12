from abc import ABC, abstractmethod
class payment(ABC):

    @abstractmethod
    def processPayment(self):
        pass


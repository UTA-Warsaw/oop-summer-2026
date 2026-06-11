from abc import ABC, abstractmethod


class OnlinePayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(OnlinePayment):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")


payment = CreditCardPayment()
payment.pay(250)
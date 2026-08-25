# Strategy Design Pattern - Library Fine Payment System

# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")


# Concrete Strategy 2
class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit/Debit Card.")


# Concrete Strategy 3
class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


# Context
class LibraryFine:
    def __init__(self, amount, payment_strategy):
        self.amount = amount
        self.payment_strategy = payment_strategy

    def make_payment(self):
        self.payment_strategy.pay(self.amount)


# Main program
fine = LibraryFine(100, CashPayment())
fine.make_payment()

fine = LibraryFine(200, CardPayment())
fine.make_payment()

fine = LibraryFine(150, UpiPayment())
fine.make_payment()

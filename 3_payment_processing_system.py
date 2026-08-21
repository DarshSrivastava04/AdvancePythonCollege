from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount) -> str:
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount) -> str:
        return f"Processing Credit Card Payment of {amount}"


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount) -> str:
        return f"Proceessing BitCoin Payment of {amount}"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount) -> str:
        return f"Processing PayPal Payment of {amount}"


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)


if __name__ == "__main__":
    credit_card = CreditCardPayment()
    bitcoin = BitcoinPayment()
    paypal = PayPalPayment()

    processor = PaymentProcessor(credit_card)

    while True:
        print("\n---- Payment Platform ----")
        print("Choose the Payment Method convenient to you from below.")
        print("1.Credit Card")
        print("2.BitCoin")
        print("3.PayPal")
        print("4.exit")

        try:
            choice = int(input("Enter serial No. of your choice :"))

            if choice == 4:
                print("Exiting the program Gracefully.")
                break

            if choice not in [1, 2, 3]:
                continue

            amount = int(input("Enter the amount you want to Process :"))

            if choice == 1:
                processor.set_strategy(credit_card)
                print(processor.process_payment(amount))

            elif choice == 2:
                processor.set_strategy(bitcoin)
                print(processor.process_payment(amount))

            elif choice == 3:
                processor.set_strategy(paypal)
                print(processor.process_payment(amount))

            else:
                print("Please enter among choices provided.")

        except ValueError:
            print("Please Enter valid values")
            continue

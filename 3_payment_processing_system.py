from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self,amount) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self,amount) -> str:
        return f"Processing Credit Card Payment of {amount}"

class BitcoinPayment(PaymentStrategy):
    def pay(self,amount) -> str:
        return f"Proceessing BitCoin Payment of {amount}"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount)-> str:
        return f"Processing PayPal Payment of {amount}"

class PaymentProcessor:
    def __init__(self,strategy):
        self.strategy = strategy
    def set_strategy(self,strategy):
        self.strategy = strategy
    def process_payment(self, amount):
        return self.strategy.pay(amount)

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    bitcoin = BitcoinPayment()
    paypal = PayPalPayment()

    processor = PaymentProcessor(credit_card)
    print("\n--- Testing Payment System ---")
    print(processor.process_payment(100))

    processor.set_strategy(paypal)
    print(processor.process_payment(250))

    processor.set_strategy(bitcoin)
    print(processor.process_payment(500))
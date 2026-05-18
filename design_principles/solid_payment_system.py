'''
Drill — SOLID (15 mins)

You're building a payment system.
Apply ALL 5 SOLID principles.

Requirements:
- Process payments (credit card, paypal)
- Send Notifiers (email, SMS)
- Log transactions

Step 1 — Create abstract base classes:
  PaymentProcessor with @abstractmethod process(amount)
  Notifier with @abstractmethod send(message)
  Logger with @abstractmethod log(message)

Step 2 — Concrete implementations:
  CreditCardProcessor(PaymentProcessor)
    process(amount) → "Processing £{amount} via Credit Card"

  PayPalProcessor(PaymentProcessor)
    process(amount) → "Processing £{amount} via PayPal"

  EmailNotifier(Notifier)
    send(message) → "Email: {message}"

  ConsoleLogger(Logger)
    log(message) → "LOG: {message}"

Step 3 — OrderService class
  __init__(self, processor, notifier, logger)
  method: checkout(amount) that:
    1. calls processor.process(amount)
    2. calls notifier.send("Payment of £{amount} received")
    3. calls logger.log("Order completed for £{amount}")
    4. returns all three strings as a list

Expected:
service = OrderService(
    CreditCardProcessor(),
    EmailNotifier(),
    ConsoleLogger()
)
service.checkout(100)
→ [
    "Processing £100 via Credit Card",
    "Email: Payment of £100 received",
    "LOG: Order completed for £100"
  ]
  '''
  
  
from abc import ABC, abstractmethod

# Step 1 — Abstract base classes
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount): pass

class Notifier(ABC):
    @abstractmethod
    def send(self, message): pass

class Logger(ABC):
    @abstractmethod
    def log(self, message): pass

# Step 2 — Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing £{amount} via Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processing £{amount} via PayPal"

class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email: {message}"

class ConsoleLogger(Logger):
    def log(self, message):
        return f"LOG: {message}"

# Step 3 — OrderService
class OrderService:
    def __init__(self, processor, notifier, logger):
        self.processor = processor
        self.notifier = notifier
        self.logger = logger

    def checkout(self, amount):
        result1 = self.processor.process(amount)
        result2 = self.notifier.send(f"Payment of £{amount} received")
        result3 = self.logger.log(f"Order completed for £{amount}")
        return [result1, result2, result3]

# Usage
service = OrderService(
    CreditCardProcessor(),
    EmailNotifier(),
    ConsoleLogger()
)
print(service.checkout(100))
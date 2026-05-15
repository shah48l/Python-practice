''' Real world example for factory pattern '''
''' Rule: Always code to interface, not implementation '''
#Step 1: Define Abstraction 
from abc import ABC,abstractmethod

# Comman contract(Interface)
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,amount: float) -> None:
        pass 
    
#Step 2: Concrete implementation 

class CardPayment(PaymentProcessor):
    def pay(self,amount: float) -> None:
        print(f"Paid ${amount} using Card")
        
class UPIPayment(PaymentProcessor):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using UPI")
        
class CashPayment(PaymentProcessor):
    def pay(self,amount: float) -> None:
        print(f"Paid ${amount} using Cash")
        
#Step 3: Factory (centralized creation)

class PaymentFactory:
    _registry = {} # -> it is a dict where it stores references and not objects 
    
    @classmethod #--> belongs to the class and the object because Factory is a GLOBAL CREATOR , not per-object logic 
    def register(cls,method:str,processor):
        cls._registry[method] = processor
        
    def create(cls,method:str) -> PaymentFactory:
        processor = cls._registry.get(method) # Client should not care about concrete class , where client only need to know what and not how 
        if not processor:
            raise ValueError(f"Unsupported payment method: {method}")
        return processor()
    
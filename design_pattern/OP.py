'''
Scenario: Order Processing System
You're building an e-commerce backend. When an order is placed, multiple independent systems need to react — send a confirmation email, update inventory, and log the event for auditing. These systems must not be coupled to the order service.
Your tasks:

Define an Observer abstract base class with an update(event: str, data: dict) method
Define a Subject base class with:

subscribe(observer: Observer) — adds an observer
unsubscribe(observer: Observer) — removes an observer
notify(event: str, data: dict) — calls update() on all observers


Implement OrderService that inherits Subject and has a place_order(order: dict) method that persists the order (just print it) then fires notify()
Implement three observers: EmailService, InventoryService, AuditLogger — each prints what it's doing when update() is called
Write a driver that wires everything together, places an order, then unsubscribes AuditLogger and places a second order to prove it no longer fires

Constraints:

OrderService.place_order() must not import or reference EmailService, InventoryService, or AuditLogger — it only calls self.notify()
Subject must store observers in a list
unsubscribe() must raise ValueError with a descriptive message if the observer isn't registered

'''

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self,event:str,data:dict):
        pass


class Subject:
    def __init__(self):
        self._observer = [] 
    
    def subscribe(self,observer:Observer):
        return self._observer.append(observer)
    
    def unsubscribe(self, observer: Observer):
        if observer not in self._observers:
            raise ValueError(f"{observer.__class__.__name__} is not subscribed")
        self._observers.remove(observer)
    
    def unsubscribe(self,observer:Observer):
        return self._observer.remove(observer)
    
    def notify(self,event:str,data:dict):
        for observer in self._observer:
            observer.update(event,data)


class OrderService(Subject):
    def place_order(self,order:dict):
        print("Order has been placed successfully")
        self.notify("ORDER_PLACE",order)
        return f"Order has been placed: {order}"
    
class EmailService(Observer):
    def update(self,event:str,data:dict):
        return f"Sending confirmation email for ->{data}"
    
class InventoryService(Observer):
        def update(self,event:str,data:dict):
            return f"InventoryService → Updating stock for {data}"

class AuditLogger(Observer):
    def update(self, event: str, data: dict):
        return f"AuditLogger → Logging {event}: {data}"


email = EmailService()
order_service = OrderService()
audit = AuditLogger()
inventory = InventoryService()

order_service.subscribe(email)
order_service.subscribe(inventory)
order_service.subscribe(audit)

print("---- First Order ----")
order_service.place_order({
    "id": 101,
    "item": "Laptop",
    "qty": 1
})


order_service.unsubscribe(audit)

print("\n---- Second Order ----")
order_service.place_order({
    "id": 102,
    "item": "Mouse",
    "qty": 2
})
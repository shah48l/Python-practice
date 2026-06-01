'''
Scenario: Notification Service
You're building a backend notification system. The app needs to send notifications via Email, SMS, and Push channels. The channel is determined at runtime from a config or request parameter.
Your tasks:

Define a Notifier abstract base class with a send(recipient: str, message: str) -> dict method
Implement EmailNotifier, SMSNotifier, PushNotifier — each returns a dict with channel, recipient, message, and status: "sent"
Build a NotifierFactory class with a create(channel: str) -> Notifier class method
Add a register(channel, cls) class method so new channels can be added without touching factory internals
Write a small driver that creates all three notifiers and sends a message through each

Constraints:

No if/elif chains inside create() — use a registry dict
Raise a descriptive ValueError for unknown channels
register() should work as a decorator too (bonus)

'''
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> dict:
        pass
    
class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> dict:
        return {
            "channel": "Email",     
            "recipient":recipient,     
            "message":message,          
            "status": "sent"          
        }

class SMSNotifier(Notifier):
    def send(self, recipient: str, message:str) -> dict:
         return {
            "channel": "SMS",     
            "recipient":recipient,     
            "message": message,          
            "status": "sent"          
        }

class PushNotifier(Notifier):
    def send(self, recipient: str, message:str) -> dict:
         return {
            "channel": "Push",     
            "recipient":recipient,     
            "message":message,          
            "status": "sent"  
         }

class NotifierFactory:
    _registry: dict = {
        "email": EmailNotifier, 
        "sms":   SMSNotifier,
        "push":  PushNotifier,
    }
        
    @classmethod
    def create(cls,channel:str) -> Notifier:
        notifier_cls = cls._registry.get(channel)
        if not notifier_cls:
            raise ValueError(f"Unknown channel: {channel}. Valiid:{list(cls._registry)}")
        return notifier_cls()
    
    # without decorator 
    # @classmethod
    # def registry(cls,channel:str,notifier_cls):
    #     cls._registry[channel] = notifier_cls
        
    #with decorator

    @classmethod
    def registry(cls,channel:str):
        def decorator(notifier_cls):
            cls._registry[channel] = notifier_cls
            return notifier_cls
        return decorator 

@NotifierFactory.register("whatsapp")
class WhatsAppNotifier(Notifier):
    def send(self, recipient: str, message: str) -> dict:
        return {"channel": "whatsapp", "recipient": recipient,
                "message": message, "status": "sent"}
    

    
if __name__ == "__main__":
    for channel in ["email", "sms", "push", "whatsapp"]:
        notifier = NotifierFactory.create(channel)
        result = notifier.send("user@example.com", "Hello!")
        print(result)

    # test unknown channel
    try:
        NotifierFactory.create("fax")
    except ValueError as e:
        print(e)
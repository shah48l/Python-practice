from abc import ABC,abstractmethod

#Step 1: Component
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    
#Step 2: Concrete Component 

class SimpleCoffee(Coffee):
    def cost(self):
        return 100
    def description(self):
        return "Simple Coffee"
   
#step 3 : Base Decorator 
class CoffeeDecorator(Coffee):
    def __init__(self,coffee:Coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()
    
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 20 
    
    def description(self):
        return self._coffee.description() + "Milk"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 10

    def description(self):
        return self._coffee.description() + ", Sugar"
    
    
coffee = SimpleCoffee()

coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

'''  

SimpleCoffee
   ↓ wrapped by
MilkDecorator
   ↓ wrapped by
SugarDecorator

'''
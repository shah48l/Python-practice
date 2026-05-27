'''
Drill — Inheritance, super(), MRO, name mangling (20 mins)

Build a vehicle system:

Class: Vehicle (base)
- __init__(self, make, speed)
  - self.make = make
  - self._speed = speed          ← protected
  - self.__engine = "V4"         ← private (name mangled)
- method: get_engine() → returns self.__engine
- method: describe() → "Vehicle: {make}, speed: {speed}"

Class: Car(Vehicle)
- __init__(self, make, speed, doors)
  - call super().__init__
  - self.doors = doors
- override describe() → "Car: {make}, {doors} doors, speed: {speed}"
- method: get_info() → calls self.get_engine() and returns
  "Engine: {engine}, Doors: {doors}"

Class: ElectricCar(Car)
- __init__(self, make, speed, doors, battery)
  - call super().__init__
  - self.battery = battery
- override describe() → "ElectricCar: {make}, battery: {battery}kWh"
- override get_engine() → "Electric Motor"

Expected:
v  = Vehicle("Toyota", 120)
c  = Car("Honda", 150, 4)
ec = ElectricCar("Tesla", 200, 4, 100)

v.describe()     → "Vehicle: Toyota, speed: 120"
c.describe()     → "Car: Honda, 4 doors, speed: 150"
c.get_info()     → "Engine: V4, Doors: 4"
ec.describe()    → "ElectricCar: Tesla, battery: 100kWh"
ec.get_info()    → "Engine: Electric Motor, Doors: 4"

print(ElectricCar.__mro__)  → ElectricCar → Car → Vehicle → object
'''

class Vehicle:
    def __init__(self,make,speed):
        self.make = make
        self._speed = speed
        self.__engine = "V4"
    
    def get_engine(self):
        return self.__engine 
        
    def describe(self):
        return f"Vehicle: {self.make}, speed: {self._speed}"
    
class Car(Vehicle):
    def __init__(self,make,speed,doors):
        self.doors = doors
        super().__init__(make,speed)
    
    def describe(self):
        return f"Car: {self.make}, {self.doors} doors, speed: {self._speed}"
    
    # method: get_info() → calls self.get_engine() and returns "Engine: {engine}, Doors: {doors}"
    def get_info(self):
        return f"Engine: {self.get_engine()}, Doors: {self.doors}"
    
    '''
    Class: ElectricCar(Car)
- __init__(self, make, speed, doors, battery)
  - call super().__init__
  - self.battery = battery
- override describe() → "ElectricCar: {make}, battery: {battery}kWh"
- override get_engine() → "Electric Motor"
'''

class ElectricCar(Car):
    def __init__(self, make, speed, doors,battery):
        super().__init__(make, speed, doors)
        self.battery = battery
        
    def describe(self):
        return f"ElectricCar: {self.make}, battery: {self.battery}kWh"
    
    def get_engine(self):
        return f"Electric Motor"
    
v  = Vehicle("Toyota", 120)
c  = Car("Honda", 150, 4)
ec = ElectricCar("Tesla", 200, 4, 100)

v.describe()     
c.describe()    
c.get_info()     
ec.describe()    
ec.get_info()    
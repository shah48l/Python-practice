'''
Drill — Abstract classes + Polymorphism (15 mins)

Create an abstract base class called Animal with:
- @abstractmethod  speak()  → returns a string
- @abstractmethod  move()   → returns a string
- Concrete method  describe() → returns:
  "I am a {class name} and I say {self.speak()}"
  Hint: use self.__class__.__name__ for the class name

Create 3 subclasses:

Dog:
  speak() → "Woof!"
  move()  → "I run on four legs"

Bird:
  speak() → "Tweet!"
  move()  → "I fly with wings"

Fish:
  speak() → "..."
  move()  → "I swim with fins"

Expected:
d = Dog()
d.speak()     → "Woof!"
d.move()      → "I run on four legs"
d.describe()  → "I am a Dog and I say Woof!"

Animal()      → raises TypeError

'''

from abc import ABC,abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass
    
    
    def describe(self):
        return f"I am a {self.__class__.__name__} and I say {self.speak()}"
    
    
class Dog(Animal):
    
    def speak(self):
        return "Woof!"

    def move(self):
        return "I run on four legs"
    
class Bird(Animal):
    
    def speak(self):
        return "Tweet!"

    def move(self):
        return "I fly with wings"

class Fish(Animal):
    
    def speak(self):
        return "...!"

    def move(self):
        return "I swim with fins"
    
    

    
    
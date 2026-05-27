'''
Problem 1
Create a base class Animal with:
- Attributes: name, age
- A method speak() that prints "Some sound"
- A __str__ that returns "Animal[name=Dog, age=3]"

Create a subclass Dog that:
- Inherits from Animal
- Overrides speak() to print "Woof!"
- Adds a method fetch() that prints "{name} fetches the ball!"

'''

class Animal :
    def __init__(self,name:str,age:int):
        self.name = name 
        self.age = age 
        
    def speak(self):
        return "Some Sound"
    
    def __str__(self):
        return f"Animal[name={self.name}, age={self.age}]"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def fetch(self):
        return f'{self.name} fetches the ball!'
    
print(Dog("Ashuthosh",22))
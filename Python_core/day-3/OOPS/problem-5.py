'''
Problem 2
Create a base class Shape with:
- A method area() that returns 0
- A method describe() that prints 
  "This shape has area: {area}"
  — call self.area() inside describe()

Create a subclass Circle that:
- Takes radius as argument
- Overrides area() to return 3.14 * radius * radius
- Has a __str__ that returns "Circle(radius=5)"

'''

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0 
    
    def describe(self):
        return f'This shape has area: {self.area()}'
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 
    
    def area(self):
        area = 3.14 * self.radius * self.radius
        return area 
        
    def __str__(self):
        return f"Circle(radius={self.radius})"
    
    
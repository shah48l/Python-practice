'''
Drill 3 — @property, getters and setters (15 mins)

Create a class called Circle with:
- A PRIVATE attribute _radius
- @property called `radius` that returns _radius
- @radius.setter that:
    - raises ValueError if radius <= 0
    - otherwise sets _radius
- @property called `area` that returns the area (read-only, no setter)
    - formula: 3.14159 * radius * radius
- @property called `diameter` that returns _radius * 2 (read-only)
- __str__ → "Circle(radius=5, area=78.53975)"

Example:
c = Circle(5)
c.radius         → 5
c.diameter       → 10
c.area           → 78.53975
str(c)           → "Circle(radius=5, area=78.53975)"

c.radius = 3     → updates radius to 3
c.radius = -1    → raises ValueError: "Radius must be positive"
c.area = 10      → raises AttributeError (no setter defined)
'''

class Circle:
    def __init__(self,radius):
        self._radius = radius 
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("Radius must be positive")
        else:
            self._radius = value
            
    @property
    def area(self):
        return 3.141159 * self.radius * self.radius 
    @property
    def diameter(self):
        return 2* self.radius
        
    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area})"
    
        
         
        
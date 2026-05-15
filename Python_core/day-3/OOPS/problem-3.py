'''
Problem 3
Create a class called Rectangle with:
- Attributes: width, height
- A method area() that returns width * height
- A method perimeter() that returns 2 * (width + height)
- A method is_square() that returns True if width == height
- A __str__ that returns:
  "Rectangle(width=4, height=6)"
'''

class Rectangle:
    def __init__(self,width:int,height:int):
        self.width = width 
        self.height = height
        
    def area(self):
        area = self.width * self.height 
        return area 
        
    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
        
    def is_square(self):
        if self.width == self.height:
            return True
        return False
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
     
'''
Problem 3
Create a class Employee with:
- Attributes: name, salary
- A method details() that returns 
  "Employee: Shahid, Salary: 50000"

Create a subclass Manager that:
- Adds an attribute: department
- Uses super() to call Employee's __init__
- Overrides details() to return
  "Manager: Shahid, Salary: 50000, Department: Engineering"
  
'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
        
    def details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"
m = Manager("Shahid", 50000, "Engineering")

print(m.details())
'''
Drill 2 — @classmethod and @staticmethod (15 mins)

Create a class called Employee with:
- Attributes: name (str), salary (float), department (str)
- __str__ → "Employee(name='Alice', department='Engineering')"

- @classmethod  called `from_string`
  Takes a string in the format "Alice,50000,Engineering"
  Parses it and returns a new Employee object

- @classmethod called `default_employee`
  Returns an Employee with name="Unknown", salary=0.0, department="General"

- @staticmethod called `is_valid_salary`
  Takes a number, returns True if salary > 0 and salary < 1_000_000

Example:
e1 = Employee("Alice", 50000, "Engineering")
e2 = Employee.from_string("Bob,60000,Marketing")
e3 = Employee.default_employee()

str(e1)   → "Employee(name='Alice', department='Engineering')"
str(e2)   → "Employee(name='Bob', department='Marketing')"
str(e3)   → "Employee(name='Unknown', department='General')"

Employee.is_valid_salary(50000)   → True
Employee.is_valid_salary(-100)    → False
Employee.is_valid_salary(2000000) → False

'''

class Employee:
    def __init__(self,name:str,salary:float,department:str):
        self.name =name
        self.salary = salary 
        self.department = department
        
    def __str__(self):
        return f"Employee(name='{self.name}', department='{self.department}')"
    
    @classmethod
    def from_string(cls,data):
        name, salary, department = data.split(",")
        return cls(name,float(salary),department)
        
    @classmethod
    def default_emplotee(cls):
        return cls("Unknown", 0.0, "General")
    
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0 and salary <1_000_000
        
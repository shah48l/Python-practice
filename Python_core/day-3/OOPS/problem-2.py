'''
Problem 2
Create a class called Student with:
- Class variable: school = "GreenTech"
- Instance variables: name, grade
- A method promote() that increases grade by 1
- A __str__ that returns:
  "Shahid (Grade 10) at GreenTech"

Example:
s = Student("Shahid", 10)
s.promote()
print(s) → "Shahid (Grade 11) at GreenTech"

'''

class Student:
    school = "GreenTech"
    def __init__(self,name:str,grade:int):
        self.name = name
        self.grade = grade
        
    def promote(self):
        self.grade +=1
        return self.grade 
    
    def __str__(self):
        return f"{self.name} (Grade {self.grade}) at {Student.school}"
        
s = Student("Shahid",10)
s.promote()
s.promote()

print(s)
        
        
            
        
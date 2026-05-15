''' The core structure while designing a Builder Pattern is that you follow 
    4 steps '''
    
# Step 1 : Product --> Final Object 

class User:
    def __init__(self):
        self.name = None
        self.age = None
        self.email = None
        self.phone = None
    
    def __str__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email}, phone={self.phone})"

# Step 2 : Builder --> step by step construction of methods 
class UserBuilder:
    def __init__(self):
        self.user = User()
        
    def set_name(self,name):
        self.user.name = name 
        return self # enables chaining
    
    def set_email(self,email):
        self.user.email = email 
        return self # enables chaining

    def set_age(self,age):
        self.user.age = age
        return self # enables chaining

    def set_phone(self, phone):
        self.user.phone = phone
        return self # enables chaining

    def build(self):
        return self.user

# Step 3: Usage 
user = (
    UserBuilder()
    .set_name("Shahid")
    .set_email("shahid@gmail.com")
    .set_age(22)
    .set_phone(87786187605)
    .build()
)

print(user)

'''8. When to use Builder Pattern

Use it when:

✅ Object has many optional fields
✅ Object creation has multiple steps
✅ You want readable code
✅ You want immutability (advanced use)
✅ Construction logic should be separate '''
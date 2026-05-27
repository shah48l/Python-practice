'''
Problem 3
Write a closure called make_greeting that takes a greeting word 
and returns a function that takes a name and prints the full greeting.

Example:
hello = make_greeting("Hello")
hello("Shahid") → "Hello, Shahid!"

hi = make_greeting("Hi")
hi("Shahid") → "Hi, Shahid!"

'''

def make_greeting(a:str):
    def add_greeting(b:str):
        return f"{a}, {b}!"
    
    return add_greeting
    
hello = make_greeting("Hello")
print(hello("Shahid"))
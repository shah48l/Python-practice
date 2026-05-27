''' Problem 2
Write a closure called make_counter that returns a function.
Every time the returned function is called, it increments 
and returns a running count starting from 0.

Example:
counter = make_counter()
counter() → 1
counter() → 2
counter() → 3
'''

def make_counter(x=0):
    def counter():
        nonlocal x
        x +=1
        return x
        
    return counter

count = make_counter()
print(count())
print(count())
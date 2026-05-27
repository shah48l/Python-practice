def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("before")
        res = func(*args, **kwargs)
        print("after")
        return res
    return wrapper
@my_decorator
def greet(name):
    print(f"hello {name}")
    
greet("Shahid")

'''
Part A — Decorator
Write a decorator called `timer` that:
- measures how long a function takes to run
- prints: "Function {name} took {time:.4f}s"
- returns the function's result unchanged

Usage:
@timer
def slow_add(a, b):
    import time
    time.sleep(0.1)
    return a + b

slow_add(2, 3)
# prints: "Function slow_add took 0.1001s"
# returns: 5
'''
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start: .4f}s")
        return res
    return wrapper
    
@timer 
def slow_add(a,b):
    time.sleep(0.1)
    return a+b

print(slow_add(2,3))
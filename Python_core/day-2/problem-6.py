'''
Problem 3
Write a lambda that takes two numbers and returns 
the larger one — without using max().
Assign it to a variable called get_max and call it.

Example: get_max(10, 3) → 10

'''

def get_max(a:int,b:int)->int:
    res = lambda a,b: a if a>b else b
    return res(a,b)
print(get_max(10,3))
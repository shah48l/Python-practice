'''
Problem 1
Use map() and a lambda to take a list of numbers 
and return a new list with each number squared.

Example: [1, 2, 3, 4] → [1, 4, 9, 16]

'''

def func(a:list):
    res = list(map(lambda x : x**2,a))
    return res 

print(func([1, 2, 3, 4]))
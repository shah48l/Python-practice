'''
Problem 1

Write a function that takes a list of integers and returns 
a new list with only the even numbers — use a list comprehension.

'''

def func(a:list)->None:
    new_list = [x for x in a if x%2==0]
    return new_list

print(func([1,2,3,4,5]))
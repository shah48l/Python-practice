'''
Problem 1
Write a function that accepts any number of integers 
and returns their sum — without using the built-in sum().

'''

def add_sum(*numbers)->int:
    total = 0
    for num in numbers:
        total += num
    return total 
        

print(add_sum(1,2,3,4,5,2,))
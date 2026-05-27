'''
Problem 2
Write a function that accepts any number of keyword arguments 
and prints each key and value on a new line like this:
name: Shahid
age: 25

'''

def func_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
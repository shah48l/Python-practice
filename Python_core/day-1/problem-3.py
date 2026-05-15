'''

Problem 3
Write a function that takes two lists and returns their 
intersection — elements in both lists — without using sets.

'''

def func(a:list,b:list)->None:
    return list(set(a) | set(b))

print(func([1,2,3,4],[3,4,5,6]))
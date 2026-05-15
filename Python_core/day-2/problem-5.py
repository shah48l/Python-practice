'''
Problem 2
Use filter() and a lambda to take a list of words 
and return only the words longer than 4 characters.

Example: ["cat", "elephant", "dog", "tiger"] → ["elephant", "tiger"]

'''

def count_str(a:list):
    res = list(filter(lambda x: len(x)>4,a))
    return res
    
print(count_str(["cat", "elephant", "dog", "tiger"]))
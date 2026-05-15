'''
Problem 3
Write a function that takes a list of strings and returns 
a new list with duplicates removed — preserving original order.
Do not use set() directly on the list.

'''

def remove_dup(a:list)->list:
    res = []
    
    for item in a:
        if item not in res:
            res.append(item)
            
    return res

print(remove_dup(["apple", "banana", "apple", "orange", "banana"]))
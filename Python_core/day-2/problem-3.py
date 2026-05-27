'''
Problem 3
Write a function called merge_dicts that accepts any number 
of dictionaries as arguments and returns a single merged dictionary.
If the same key exists in multiple dicts, the last one wins.

Example:
merge_dicts({"a": 1}, {"b": 2}, {"a": 99}) → {"a": 99, "b": 2}

'''

def merge_dicts(*dict):
    res = {}
    for d in dict:
        res.update(d)
    return res
    
print(merge_dicts({"a": 1}, {"b": 2}, {"a": 99}))
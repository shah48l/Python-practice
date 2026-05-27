'''
Problem 4
Write a function that takes a sentence (string) and returns 
the most frequent word. If there's a tie, return any one of them.
Example: "the cat sat on the mat the" → "the"

'''

def dict_func(a: str) -> str:
    res = {}
    
    for word in a.split():          # blank 1: split into words
        res[word] = res.get(word, 0) + 1   # blank 2: same pattern as P2
        
    return max(res, key=lambda word: res[word])      # blank 3: what do we rank by?
'''
Problem 2
Write a function that takes a string and returns a dictionary 
of character frequencies (how many times each character appears).

'''

# def func(a:str)->None:
#     res = {}
    
#     for char in a:
#         if char in res:
#             res[char]+=1
#         else:
#             res[char] = 1
#         pass


def func(a: str) -> dict:
    res = {}
    for char in a:
        res[char] = res.get(char,0) + 1        # fill this in using res.get()
    return res

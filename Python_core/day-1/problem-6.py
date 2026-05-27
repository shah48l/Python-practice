'''
Problem 2
Write a function that takes a string and returns True 
if it is a palindrome, False otherwise.
Ignore spaces and case. Example: "Race car" → True

'''

# def pal_func(a: str, b: str) -> bool:
#     return sorted(a.lower()) == sorted(b.lower())

# print(pal_func("Race", "Car"))

def pal_func(a:str) -> bool:
    a = a.lower().replace(" ","")
    
    l = 0
    r = len(a)-1
    
    while l<r:
        if a[l]!=a[r]:
            return False

        l+=1
        r-=1
        
    return True

print(pal_func("race care"))
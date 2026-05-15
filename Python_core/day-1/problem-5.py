'''
Problem 1
Write a function that takes a string and returns it reversed
— without using slicing [::-1] or reversed().

'''

def reverse_func(a:str)->None:
    a = list(a)
    l = 0
    r = len(a)-1
    
    while l<r:
        a[l],a[r] = a[r],a[l]
        l+=1
        r-=1
        
    return "".join(a)
        
    
print(reverse_func("hello"))
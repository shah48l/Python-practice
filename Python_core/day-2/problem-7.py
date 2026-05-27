'''Problem 1
Write a closure called make_multiplier that takes a number n 
and returns a function that multiplies any number by n.

Example:
triple = make_multiplier(3)
triple(5) → 15
'''

def make_multiplier(x:int):
    def triplet(y:int):
        res = x * y
        return res
    return triplet
triple = make_multiplier(3)
print(triple(5))
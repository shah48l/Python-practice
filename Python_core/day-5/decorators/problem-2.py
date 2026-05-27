'''
Part B — Generator
Write a generator called `fibonacci` that:
- yields fibonacci numbers infinitely
- caller controls how many they take

Usage:
gen = fibonacci()
[next(gen) for _ in range(7)]
→ [0, 1, 1, 2, 3, 5, 8]


'''

def fibonacci():
    a, b = 0,1
    while True:
        yield a 
        a,b = b,a+b
gen = fibonacci()
[next(gen) for _ in range(7)]
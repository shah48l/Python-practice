''' Lambda function is a small anonymoys function(no name)
 written in a single line'''
 
add = lambda a,b : a+b
print(add(2,3))

def add(a,b):
    return a+b

'''Lambda can appear where def is not allowed'''
# Here am passing a function without defining it seperately 
nums = [1,2,3]
res = list(map(lambda x: x * 2, nums))

# Inside a DS

function = [
    lambda x: x+1,
    lambda x: x*2
]
''' --> Here you can store a function inline'''
print(function)


config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
 }

#accessing a Value through its Key 
print(config["color"])

config["font"] = "helvetica"
print(config)

# class Number:
#     def __init__(self,value):
#         self.value = value
    
# print(Number(42).__dict__)

'''
d[key] -> raises KeyError if missing 
.get(key, default) -> safe access,no error 
d[key] = value -> add or updqate 
.setdefault(key,default) -> adds key only if missing 
.update(other) -> bulk merge 

Removing data 

.pop(key) -> removes and returns the value 
.popitem() -> removes last inserted pair (LIFO)
del d[key] -> removes without returning 
.clear() -> empties the dict 

iteration 

Keys : for k in d or for k in d.keys()
values: for v in d.values()
Both : for key,value in d.items()

sort by values 

dict(sorted(students.items, key = lambda x : x[1]))
dict(sorted(students.items, key = lambda x: x[1, reverse = true]))

sort by keys 

dict(sorted(dict_name.items(), keyk=lambda x: x[0]))

'''
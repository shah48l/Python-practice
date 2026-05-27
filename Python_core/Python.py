'''Write a function analyze_collection(data) that:

Accepts any iterable
Returns a dictionary with keys: "type", "length", "unique_count", "sorted_items"
sorted_items should handle mixed types gracefully (no crash if ints and strings are mixed — sort by string representation)

Constraints:

Single function, no imports needed
Must handle: list, tuple, set, string, dict (treat dict as its keys)
Return None if input is not iterable'''

def analyze_collection(data:dict) -> None:
    if not hasattr(data,dict):
        return None 
    type_name = type(data).__name__
    
    if isinstance(data,dict):
        items = list(data.keys())
        
    else:
        items = list(data)
        
    return {
        "type":type_name,
        "length":len(data),
        "unique_count":len(set(data)),
        "sorted_items": sorted(data,key = lambda item: item[1])
    }
    
'''Write a function flatten_and_filter(nested, threshold) that:

Takes a deeply nested list (any depth) and a number threshold
Recursively flattens the list (no imports, no itertools)
Returns only elements that are numbers greater than threshold
Returns result sorted in descending order


Constraints:

Must use recursion for flattening — no loops that cheat with a stack manually
Non-number elements (strings, None, etc.) should be silently ignored
Single function is fine, or a helper — your call'''

def flatten_and_filter(nested, threshold):

    def flatten(data, result):
        for item in data:
            if isinstance(item, list):
                flatten(item, result)
            else:
                result.append(item)
        return result

    flat = flatten(nested, [])

    filtered = [
        item for item in flat
        if isinstance(item, (int, float))
        and not isinstance(item, bool)
        and item > threshold
    ]

    return sorted(filtered, reverse=True)


'''List comprehensio'''
res = [] 

for x in range(10):
    if x%2 == 0:
        res.append(x)

# list comprehension 
res = [ x for x in range(10) if x%2 == 0 ] # ordered allows duplicates 


        
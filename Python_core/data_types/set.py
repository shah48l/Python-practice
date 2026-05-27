s = {1,2,3}

s.add(4) #adds a element 
s.discard(10) # removes the element if present and raises no error 
s.pop()# removes + return arbitary element
s.remove(2) # removes , KeyError if element is missing 
s.clear() # Empties the list 
2 in s # True -> O(1) 
s.issubset({1,2,3,4})   # True
s.issuperset({1})       # True
s.isdisjoint({5,6})     # True — no overlap

print(s)


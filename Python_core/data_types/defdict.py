#Frequency Counter

from collections import Counter,defaultdict
s = "aabbbcc"

#Using counter
print(Counter(s))

#Defaultdict
freq = defaultdict(int)
for c in s:
    freq[c]+=1
    
# dict.get
freq = {}
for c in s:
    freq[c] = freq.get(c,0) + 1
    
#Grop by pattern
words = ["apple", "ant", "banana", "bat", "cherry"]

by_letter = defaultdict(list)

for w in words:
    by_letter[w[0]].append(w)
    
print(dict(by_letter))
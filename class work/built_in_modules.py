
from itertools import combinations , permutations
from collections import deque

print(list(combinations([1,2,3,4,5],3)))
print(list(permutations([1,2,3,4,5],3)))

l=[3,4,5,1,2]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        print(f"{l[i]},{l[j]}")


d = deque(l)
print(d)
print(d.pop())
d.append(6)
print(d)
print(d.popleft())
d.append(12) 
print(d)

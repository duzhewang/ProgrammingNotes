Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem

Python3:


```python
from itertools import permutations

s,n=input().split()
l=list()
for i in permutations(sorted(s), int(n)):
    l.append(''.join(i))
print(*l, sep="\n")    


```

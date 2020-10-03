Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem

```python

from itertools import combinations

S, k=input().split()

for i in range(1, int(k)+1):
    for j in combinations(sorted(S), i):
        print("".join(j))


  

```

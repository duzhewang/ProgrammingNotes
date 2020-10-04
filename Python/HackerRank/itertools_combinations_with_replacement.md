Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

```python

S, k=input().split()

from itertools import combinations_with_replacement

for j in list(combinations_with_replacement(sorted(S), int(k))):
    print("".join(j))


```

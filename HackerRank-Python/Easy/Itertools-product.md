Problem: https://www.hackerrank.com/challenges/itertools-product/problem

Python3:

```python
from itertools import product

A=list(map(int, input().split()))
B=list(map(int, input().split()))

print(*product(A, B))


```
- * is the unpack operator. 

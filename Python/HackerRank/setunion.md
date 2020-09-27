Problem: https://www.hackerrank.com/challenges/py-set-union/problem


```python
n=int(input())
A=set(map(int,input().split()))
b=int(input())
B=set(map(int, input().split()))

print(len(A.union(B)))

```

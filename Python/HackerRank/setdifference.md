Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

```python

n=int(input())
A=set(map(int, input().split()))
b=int(input())
B=set(map(int, input().split()))

print(len(A.difference(B)))

```

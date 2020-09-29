Problem: https://www.hackerrank.com/challenges/py-check-subset/problem

```python

N=int(input())
for i in range(N):
    num_A=int(input())
    A=set(map(int, input().split()))
    num_B=int(input())
    B=set(map(int, input().split()))
    print(A.issubset(B))

    


```

Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem

```python
K=int(input())
arr=list(map(int, input().split()))

print((sum(set(arr))*K-sum(arr))//(K-1))

```

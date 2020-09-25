Problem: https://www.hackerrank.com/challenges/no-idea/problem

```python
def happiness(arr, A, B):
    print(sum([(i in A)-(i in B) for i in arr]))

n, m=map(int, input().split())
arr=list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))

happiness(arr, A, B)



```

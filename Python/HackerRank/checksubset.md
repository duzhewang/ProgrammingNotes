Problem: https://www.hackerrank.com/challenges/py-check-subset/problem

- The first method: use ```issubset```
```python

N=int(input())
for i in range(N):
    num_A=int(input())
    A=set(map(int, input().split()))
    num_B=int(input())
    B=set(map(int, input().split()))
    print(A.issubset(B))

    


```

- The second method

```python
N=int(input())
for i in range(N):
    num_A=int(input())
    A=list(map(int, input().split()))
    num_B=int(input())
    B=list(map(int, input().split()))
    if all(a in B for a in A):
        print(True)
    else:
        print(False)    



```

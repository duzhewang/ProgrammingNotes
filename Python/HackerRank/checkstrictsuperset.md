Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem


```python
A=set(map(int, input().split()))
n=int(input())
result=[]
for i in range(n):
    B=set(map(int, input().split()))
    if B.issubset(A) and len(B)<len(A):
       result.append(True)
    else:
       result.append(False)
print(all(result))           
```

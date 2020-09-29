Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem

```python

n=int(input())
A=set(map(int, input().split()))
N=int(input())
for i in range(N):
    (command, newset)=(input().split()[0], set(map(int, input().split())))
    getattr(A,command)(newset)

print(sum(A))

```

- ```getattr```: https://www.programiz.com/python-programming/methods/built-in/getattr

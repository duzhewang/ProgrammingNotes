Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

```python
n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    eval("s.{}({})".format(*input().split()+[""]))
    
print(sum(s))





```

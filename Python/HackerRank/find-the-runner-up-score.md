https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

 
arr=list(arr)
z=max(arr)
while max(arr)==z:
      arr.remove(max(arr))
print(max(arr))




```

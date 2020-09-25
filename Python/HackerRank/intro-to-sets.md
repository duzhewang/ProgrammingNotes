Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

```python
def average(arr):
    average=sum(set(arr))/len(set(arr))
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


```

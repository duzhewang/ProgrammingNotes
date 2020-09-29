Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem

- The first method: 

```python
K=int(input())
arr=list(map(int, input().split()))

print((sum(set(arr))*K-sum(arr))//(K-1))

```


- The following alternative method uses two ideas:
  - how to count frequency in a list
  - how to return the key for a given value in a dictionary


```python

def CountFrequency(my_list):
    freq={}
    for item in my_list:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    return freq

def get_key(freq, val):
    for key, value in freq.items():
        if value==val:
            return key


K=int(input())
arr=list(map(int, input().split()))

print(get_key(CountFrequency(arr), 1))



```

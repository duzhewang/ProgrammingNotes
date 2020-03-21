Problem: https://www.hackerrank.com/challenges/text-wrap/problem

Python3:

```python
def wrap(string, max_width):
    l=list()
    for i in range(0, len(string), int(max_width)):
        l.append(string[i:(i+max_width)])
    return "\n".join(l)    

 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


```

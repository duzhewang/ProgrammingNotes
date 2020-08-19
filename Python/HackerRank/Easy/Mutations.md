Problem: https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Python:

```python
def mutate_string(string, position, character):
    l=list(string)
    l[position]=f'{character}'
    string=''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
```



```python
def mutate_string(string, position, character):
    string=string[:position]+f'{character}'+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)




```

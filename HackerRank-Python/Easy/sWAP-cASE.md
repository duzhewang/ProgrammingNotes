Problem: https://www.hackerrank.com/challenges/swap-case/problem

Python:

```python
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```


```python
def swap_case(letter):
    if letter.isupper():
       letter.lower()
    if letter.islower():
       letter.upper()
    return(letter)   

def main():
    s=input()
    print(''.join(map(swap_case, s)))
    
if __name=='__main__':    
   main()
```

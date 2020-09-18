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


- swapcase(): https://www.geeksforgeeks.org/python-string-swapcase/
- is.upper(), is.lower(), string.lower(), string.upper()
- string.join(iterable): https://www.w3schools.com/python/ref_string_join.asp

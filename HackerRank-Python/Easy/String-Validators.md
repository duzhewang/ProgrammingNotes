Problem: https://www.hackerrank.com/challenges/string-validators/problem

python3:

```python
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
```

- string.isalnum()
- string.isalpha()
- string.isdigit()
- string.islower()
- string.isupper()
- any(iterable): The any() function returns True if any item in an iterable are true, otherwise it returns False. If the iterable object is empty, the any() function will return False.


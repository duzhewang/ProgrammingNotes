Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem


```python
import cmath 
c=complex(input())
print(abs(complex(c.real, c.imag)))
print(cmath.phase(complex(c.real, c.imag)))

```


```python
import cmath 
c=complex(input())
print(*cmath.polar(c), sep="\n")
```

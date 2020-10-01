Problem: https://www.hackerrank.com/challenges/find-angle/problem

```python
import math
AB, BC=float(input()), float(input())
hype=math.hypot(AB, BC)
deg=round(math.degrees(math.acos(BC/hype)))
print(deg, chr(176), sep="")


```

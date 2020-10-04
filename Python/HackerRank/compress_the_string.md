Problem: https://www.hackerrank.com/challenges/compress-the-string/problem

```python
from itertools import groupby
print(*[(len(list(k)), int(c)) for c, k in groupby(input())])

```

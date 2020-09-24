https://www.hackerrank.com/challenges/capitalize/problem



```python
def solve(s):
    s=s.split()
    print(s[0][0].upper()+s[0][1:]+" "+s[1][0].upper()+s[1][1:])

solve("chris alan")    


def solve2(s):
     for x in s.split():
         s=s.replace(x, x.capitalize())
     return s    

print(solve2("hello world"))        
    


```

Problem: https://www.hackerrank.com/challenges/python-lists/problem

Pyhton3: 
``
n=int(input())
a=[]
for _ in range(n):
    c=input().strip()
    if c=='print':
        print(a)
    else: 
        c=c.split()
        if len(c)==3:
            getattr(a, c[0])(int(c[1]), int(c[2]))
        elif len(c)==2:
            getattr(a, c[0])(int(c[1]))
        else: 
            getattr(a, c[0])()
``

- strip(): 
- split():https://www.tutorialspoint.com/python3/string_strip.htm
- getattar(object, attribute): https://www.w3schools.com/python/ref_func_getattr.asp

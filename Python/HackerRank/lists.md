Problem: https://www.hackerrank.com/challenges/python-lists/problem

Pyhton3: 
```python
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
```

```python
n=int(input())
a=[]
for _ in range(n):
    c=input().strip()
    if c=='print':
        print(a)
    else: 
        c=c.split()
        if c[0]=='insert':
            a.insert(int(c[1]), int(c[2]))
        elif len(c)==2:
             if c[0]=='remove':
                a.remove(int(c[1]))
             if c[0]=='append':
                a.append(int(c[1]))   
        else: 
            if c[0]=='sort':
                a.sort()
            if c[0]=='pop':
                a.pop()
            if c[0]=='reverse':
                a.reverse()    
```                

```python
if __name__ == '__main__':
    l=[]
    N = int(input())
    for _ in range(N):
        cmd,*args=input().split()
        if cmd!="print":
            cmd=cmd+"("+",".join(args)+")"
            eval("l."+cmd)
        else:
            print(l)  

```




- strip(): 
- split():https://www.tutorialspoint.com/python3/string_strip.htm
- getattar(object, attribute): https://www.w3schools.com/python/ref_func_getattr.asp

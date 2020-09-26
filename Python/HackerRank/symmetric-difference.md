Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem

```python
M=int(input()) 
A=set(map(int, input().split()))
N=int(input())
B=set(map(int, input().split()))


print(*sorted(A^B, key=int), sep="\n")  # * is used to unpack values

```


Note: ```*``` in the print function is used to unpack values in the list. See more at https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

import turtle
import math

bob=turtle.Turtle()

"""
bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
"""

"""
for _ in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()
"""

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 200)


def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)
polygon(bob, 100, 5)



def circle(t, r):
    circumference=2*math.pi*r
    n=50
    length=circumference/n
    polygon(t, length, n)

circle(bob, 10)

# Exercise 3.1

def right_justify(s):
    return " "*(70-len(s))+s

print(right_justify("monty"))


# Exercise 3.2

## Part 1

def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print_spam)

## Part 2

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_spam(arg):
    print(arg)

do_twice(print_spam, "spam")


## Part 3

def print_twice(bruce):
    print(bruce)
    print(bruce)


## Part 4

do_twice(print_twice, "spam")


## Part 5

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print, "hello")

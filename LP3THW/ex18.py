# names, variables, code, functioins


## function 1
def print_two(*args):  # *args tell python to take all the arguments to the function and then put them in args in a list.
    arg1, arg2=args  # unpacks the arguments
    print(f"arg1: {arg1}, arg2: {arg2}")

# function 2
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# function 3
def print_one(arg1):
    print(f"arg1: {arg1}")


# function 4
def print_none():
    print("I got nothing.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

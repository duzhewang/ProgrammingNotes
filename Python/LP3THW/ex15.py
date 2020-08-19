# get input from a user: input or argv
from sys import argv
script, filename=argv
txt=open(filename)  # input the file
print(f"Here's your file {filename}:")
print(txt.read())   # print the file
print("Type the filename again:")
file_again=input(">")
txt_again=open(file_again)
print(txt_again.read())

from sys import argv

script, filename=argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target=open(filename, 'w')  # open the file for writing and name the file as target
print("Truncating the file. Goodbye!")
target.truncate()    # empties the target file
print("Now I'm going to ask you for three lines.")
line1=input("line 1:")  # input the firest line
line2=input("line 2:")  # input the second line
line3=input("line3:")   # input the third line
print("I'm going to write these to the file.")

target.write(line1)  # write the first line in file
target.write("\n")   # start a new line
target.write(line2)  # write a second line in file
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # close the file, just like saving the file

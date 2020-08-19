# goal: write a python script to copy one file to another

from sys import argv
from os.path import exists   # os.path: common pathname manipulation

script, from_file, to_file=argv

print(f"Copying from {from_file} to {to_file}")

#in_file=open(from_file)
#indata=in_file.read()

indata=open(from_file).read()  # why do I need to write in this way?


print(f"The input file is {len(indata)} bytes long.")
print(f"Does the output file exists? {exists(to_file)}") # check if the to_file exists. return True or False
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file=open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
#in_file.close()

- how to stop a python program in terminal? 
  use control+c. 
- use **exit(0)** to make the program abort. (see ex35 in LP3THW)
- use **command+/** to comment or uncomment python scripts 
- Python uses **indentation** to indicate a block of code.
- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
  - A variable name must start with a letter or the underscore character
  - A variable name cannot start with a number
  - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )  
  - Variable names are case-sensitive (age, Age and AGE are three different variables)

- The global keyword: Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword.

```
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

- Python has the following data types built-in by default, in these categories:
  - Text Type:	str
  - Numeric Types:	int, float, complex
  - Sequence Types:	list, tuple, range
  - Mapping Type:	dict
  - Set Types:	set, frozenset
  - Boolean Type:	bool 
  - Binary Types:	bytes, bytearray, memoryview

- [Difference between lists and tuples](https://www.afternerd.com/blog/difference-between-list-tuple/)

- Random numbers: Python does not have a random() function to make a random number, but Python has a built-in module called **random** that can be used to make random numbers:

```
import random
print(random.randrange(1,10)) # display a random number between 1 and 9
```


The following materials are from Scipy Lecture notes when I learn Pyhton myslef. 

-Python is a **programming language**, some features are:
1. an interpreted language. (as opposed to compiled)
2. a free softare released under an **open-source** license.
3. **multi-platform**

-Start the ipython shell by typing "iypthon" from a linux/mac terminal. 
*type( )* to check the type of the variable, for example, integers, strings.

```
>>> a = 1.5 + 0.5j
>>> a.real
1.5
>>> a.imag
0.5
>>> type(1. + 0j)   
<type 'complex'>
>>> 3 > 4
False
>>> test = (3 > 4)
>>> test
False
>>> type(test)      
<type 'bool'>
```

- a list is an ordered collection of objects.  **indexing starts at 0**.Note that **colors[start:stop]** contains the elements with **indices i such as start<= i < stop (i ranging from start to stop-1)**. Therefore, colors[start:stop] has (stop - start) elements. **Slicing syntax:** colors[start:stop:stride]
```
>>> colors = ['red', 'blue', 'green', 'black', 'white']
>>> type(colors)     
<type 'list'>
>>> colors[2]
'green'
>>> colors[-1]
'white'
>>> colors[-2]
'black'
```


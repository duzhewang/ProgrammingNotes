## [Python resources](http://pages.stat.wisc.edu/~sraschka/teaching/stat451-fs2020/)

- Python for Beginners (Video Lectures): A great video series by educators at Microsoft, which was recently made available for free on YouTube: https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6.

- Learn Python (Interactive Tutorials): On https://www.learnpython.org/, you can find a interactive exercises that help you learn Python through a sequence of coding exercises.

- Illustrated Guide to Python (Book): 
   - “Illustrated Guide to Python 3: A Complete Walkthrough of Beginning Python with Unique Illustrations Showing how Python Really Works. Now covering Python 3.6 (Treading on Python) (Volume 1)” by Matt Harrison, ISBN-13: 978-1977921758.
   - For instance, another great book is Allen Downey’s Think Python 2e (free PDF available at https://greenteapress.com/wp/think-python-2e/).
   - Python Like You Mean It: A short, free intro for getting started with Python and its main scientific computing libraries: https://www.pythonlikeyoumeanit.com.








## Python Packages
- install: in terminal, type:
```
python3 -m pip install packagename
```
- upgrade:
```
python3 -m pip install packagename -upgrade
```
- check what packages are installed in my laptop:
```
  python3 -m pip freeze
```
or directly use
```
pip freeze
```

- You can use pip commands with grep command to search for any specific module installed on your system.
```
pip list | grep <module_name_you_want_to_check>
```




## Anaconda or miniconda

- Step 1: To use the Anaconda or Miniconda distribution, download the respective installer from the anaconda.com website
and follow the instructions there. The Miniconda installer is available from https://docs.conda.io/en/latest/miniconda.html.

- Step 2: install and update python packages. For example, to install Numpy, use

```
conda install numpy
```
to update Numpy, use
```
conda update numpy
```
to uninstall Numpy, use
```
conda uninstall numpy
```

While most major packages for scientific computing are available via conda, we may find
that we need packages that are not available through the conda installer. But we can use `conda-forge`. For example, to install `mlxtend`, use

```
conda install mlxtend -c conda-forge
```
here `-c` is the channel flag.

- See how to manage environments at https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/03_python/03-python__notes.pdf.






## Python General Notes

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

- The **strip()** method removes any whitespace from the beginning or the end of a string.
```
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```
- The lower() method returns the string in lower case. The upper() method returns the string in upper case.
- [More on strings](https://www.w3schools.com/python/python_strings.asp)

- Note on class:
  - https://www.w3schools.com/python/python_classes.asp
  - https://www.hackerearth.com/zh/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/
  - example:

```
  class Person:
        def __init__(self, name, age):
           self.name = name # define attributes
           self.age = age
        def myfunc(self):
            print("Hello my name is " + self.name)
  p1 = Person("John", 36)
  p1.myfunc()
```  
- list comprehension
  ```
  x = int(input())
  y = int(input())
  z = int(input())
  n = int(input())
  print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k)!=n)])
  ```
- keep 2 decimal places
```
a=13.946
print("%.2f"% a)
```

- string format: https://pyformat.info/ and https://mkaz.blog/code/python-string-format-cookbook/#f-strings

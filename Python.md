- how to stop a python program in terminal?

  use control+c. 











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


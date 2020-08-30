## Launching IPython 

- Ipython Shell: In the command line, type 
```
ipython 
```
- Jupyter Notebook: 

```
jupyter notebook
```

## Help in IPython 

- Accessing Documentation: for example, if we want to see the documentation of the built-in ```len``` function, we can do

```
help(len)
```
or 

```
len?
```

- Accessing Source Code: for example, we can define a square function 

```
def square(a):
    """Return the square of a."""
    return a**2
```

then  we can use ```square??``` to access the source code of this function. 

## Tab-Completion

We can use the ```<TAB>``` key for auto-completion and exploration of the contents of objects, modules, and name-spaces. 

## Wildcard matching

Ipython provides a means of wildcard matching for names using the ```*``` character. The ```*``` character matches any string, including the empty string. For example, 

```
*Warning?
```


## Keyboard shortcuts in the IPython shell

| Keystroke     | Action        | 
| ------------- |:-------------:| 
| Ctrl-a        | move cursor to the beginning of the line  | 
| Ctrl-e        | move cursor to the end of the line    |  
| Ctrl-b        | move cursor back one character   |  
| Ctrl-f        | move cursor forward one character |
| Ctrl-d         | delete next character in line |
| Ctrl-k   | cut text from cursor to end of line |
| Ctrl-u   | cut text from beginning of line to the cursor |
| Ctrl-y   | Yank (i.e., paste) text that was preciously cut|
| Ctrl-t   | Transpose (i.e., switch) previous two characters |
| Ctrl-p   | Access previous command in history  |
| Ctrl-n   | Access next command in history      |
| Ctrl-r   | Reverse-search through command history |
| ```Ctrl-l```   | Clear terminal screen   |
| ```Ctrl-c```   | Interrupt current Python command |
| ```Ctrl-d```   | Exit IPython Session            |


## Magic commands 

Ipython's magic commands are designed to succinctly solve various common problems in standard data analysis. Magic commands come in two flavors: line magics, which are denoted by a single ```%``` prefix and operate on a single line of input, and cell magics, which are denoted by a double ```%%```prefix and operate on multiple lines of input. 

Some examples include: 

- [Pasting code blocks: ```%paste``` and ```%cpaste```](https://jakevdp.github.io/PythonDataScienceHandbook/01.03-magic-commands.html)

- Running external code: 

```
%run scriptname.py
```

- Timing code execution using ```%timeit```: for example, 

```
%timeit L=[n**2 for n in range(1000)]
```

The benefit of %timeit is that for short commands it will automatically perform multiple runs in order to attain more robust results. For multi line statements, adding a second % sign will turn this into a cell magic that can handle multiple lines of input. For example, here's the equivalent construction with a for-loop

```
%%timeit
   ...: L = []
   ...: for n in range(1000):
   ...:     L.append(n ** 2)
   ...: 
```


- Help on magic functions: ```%magic``` or ```%lsmagic```


# Input and Output history

- IPython's ```In``` and ```Out``` objects:  

```
print(In)
print(Out)
```

- Underscore shortcuts and previous outputs:  
 
```
print(_)
```

- Suppresing output: use a semicolon to the end of the line


- Accessing a batch of previous inputs at once:

```
%history somenumber1-somenumber2
```
or 

```
%history -n somenumber1-somenumber2
```

use ```%history?``` to see other flags. 


# Ipython and shell commands

- Shell commands in Ipython

Any command that works for the command-line can be used in Ipython by prefixing it with the ```!``` character. For example, 
```
!ls
```

-  Passing values to and from the shell

For example:
```
contents=!pwd
print(contents)
```

Note these results are not returned as lists, but as a special shell return type defined in Ipython. 


Another example (passing Python variables into the shell):

```
message="hello from python"
! echo {message}

```

- Shell-related magic commands

We can not use !cd to navigate the filesystem. But we can use 

```
%cd ...
```
or 

```
cd ...
```









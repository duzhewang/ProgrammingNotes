## Launching the IPython Shell

In the command line, type 
```
ipython 
```
## Launching the Jupyter Notebook

```
jupyter notebook
```

## Help and Documentation in IPython 

- Accessing Documentation with ```?```

```
help(...)
```

use **q** to quit help. 


```
len?
```

- Accessing Source Code with ```??```

```
def square(a):
    """Return the square of a."""
    return a**2

square??
```

## Exploring Modules with Tab-Completion 

- Tab-completion of object contents 

```
L.<TAB>
```
- Tab-completion when importing 

- Beyond tab completion: wildcard matching 

For example, 

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
| Ctrl-l   | Clear terminal screen   |
| Ctrl-c   | Interrupt current Python command |
| Ctrl-d   | Exit IPython Session            |


## Magic commands 

- [Pasting code blocks: ```%paste``` and ```%cpaste```](https://jakevdp.github.io/PythonDataScienceHandbook/01.03-magic-commands.html)

- Running external code: 
```
%run scriptname.py
```

- Timing code execution: ```%timeit```

For example, 

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





# Introduction to NumPy

```
import numpy
numpy.__version__
```

## Understanding data types in Python

- Python is dynamic typing. While a statically-typed language like C or Java requires each variable to be explicitly declared, a dynamically-typed language like Python skips this specification. 

- Unlike Python lists, NumPy is constrained to arrays that all contain the same type. If types do not much, NumPy will upcast if possible (for example, integers may be upcast to floating point. )

```
np.array([3.14, 4, 2, 3])
```

If we want to explicitly set the data type of the resulting array, we can use the ```dtype``` keyword:

```
np.array([1,2,3,4], dtype='float32)
```

- Unlike Python lists, NumPy arrays can explicitly be multi-dimensional. 

- Creating Arrays from scratch:

```
np.zeros(10, dtype=int)
```

```
np.ones((3,5), dtype=float)
```

```
np.full((3,5), 3.14)
```

```
np.arrange(0, 20, 2) # starting from 0, ending at 20, stepping by 2
```

```
np.linspace(0, 1, 5)  # an array of five values evenly spaced between 0 and 1
```


```
np.random.random((3,3))  # 3*3 array of uniformly distributed random values between 0 and 1 
```


```
np.random.normal(0 ,1, (3,3))  # 3*3 array of normally distributed random values with mean 0 and standard deviation 1
```

```
np.random.randint(0, 10, (3,3))  #3*3 array of random integers in the interval [0, 10)
```

```
np.eye(3)  # 3*3 identity matrix
```

- NumPy standard data types: https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html


## The basics of NumPy arrays 

- 




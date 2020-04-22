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



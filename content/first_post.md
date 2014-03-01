Title: Embarrassing First Post
Date: 2014-02-28 23:42
Category: Python
Tags: Python, Useless
Author: Charlie Mills
Summary: Wasting my time with Fibonacci 

This post serves no purpose other than to fill the inevitable void. Last week at an interview I was asked to write a Fibonacci function, it seems regurgitation of Computer Science theory makes you employable, so here they are in Python.

#### Recursive
```python
def f(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return f(n-1) + f(n-2)
```

#### Iterative
```python
def f(n):
    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
    return a
```

Please revel in the usefulness of these numbers (excuse the bitterness).
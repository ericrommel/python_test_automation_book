# Section 2: Tuples

## Introduction:
* Used to store collections of heterogeneous data (any type of data in the same tuple
* Tuples are `immutable` sequences, useful for storing fixed sets of data that should not change during execution.
* Round brackets ()
* Only two built-in method:
    count()	Returns the number of times a specified value occurs in a tuple
    index() Searches the tuple for a specified value and returns the position of where it was found
* Uses less memory and are faster to access than to lists



## References:

1. [Tuples - Python Documentation](https://docs.python.org/3/tutorial/introduction.html#tup)
2. [Python Tuples - Real Python](https://realpython.com/python-tuples/)

---

## 2.1 Understanding Tuples

Tuples can store multiple items in a single variable. Their immutability makes them suitable for storing constants.


### Syntax:

Creating

```python
my_tuple = ()
my_tuple = (21, 12, 33)
# from list
tuple_from_list = tuple([11, 22, 33])
```

Access to element by integer index

```python
print(my_tuple[2]) # returns 12
```


### Example:

```python
http_status_codes = (200, 404, 500)
```


## Hands-On Task:

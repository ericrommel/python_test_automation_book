# Section 2: Tuples

## Introduction:
* Used to store collections of heterogeneous data (any type of data: string, boolean, etc)
* Round brackets ()
* Tuple is `immutable` - can't be changed
* Only two built-in method:
    count()	Returns the number of times a specified value occurs in a tuple
    index() Searches the tuple for a specified value and returns the position of where it was found
* Uses less memory and is faster to access to elements vs list
* Tuple is `immutable`, therefore is useful for storing fixed sets of data that should not change during execution (contant).



## References:

1. [Tuples - Python Documentation](https://docs.python.org/3/tutorial/introduction.html#tup)
2. [Python Tuples - Real Python](https://realpython.com/python-tuples/)

---


### Syntax:

Creating
```python
my_tuple = ()
my_tuple = (21, 12, 33)
# from list
tuple_from_list = tuple([11, 22, 33])
# from any sequence of elements (e.g. range)
tuple_from_range = tuple(range(10))
```

Access to element by integer index

```python
print(my_tuple[2]) # returns 12
```


## Hands-On Task:

1. Create a tuple with several following types of elemenents: integer, boolean, list, tuple, string.
2. Define type of 3d element of tuple
3. Add new element into the tuple.
4. Get tuple that contains sorted elements of initial tuple e.g. tuple_to_find_largest = (2, 6, 4, 17, 9, 3, 15, 7)
5. Get tuple that contains two largest elements of initial tuple e.g. tuple_to_find_largest = (2, 6, 4, 17, 9, 3, 15, 7)

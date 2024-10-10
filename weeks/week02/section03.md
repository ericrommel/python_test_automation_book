# Section 3: Dictionaries

A dictionary is a mutable mapping object of key-value pair items, perfect for storing related data and efficient data 
retrieval. A dictionary can grow and shrink. It may be nested and contain other collection data types and other 
dictionaries. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys.

An object of any immutable type can be used as a dictionary key. Duplicate key are not allowed. By contrast, 
a dictionary value can be any type of object Python supports, and it can appear in a dictionary multiple times.

A dictionary is presented with class `dict`.


## References:

1. [Dictionaries - Python Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
2. [Python Dictionaries - Real Python](https://realpython.com/python-dicts/)
3. [Mapping Types - dict - Python Documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

---

Dictionaries stores data in key-value pairs. The main operations on a dictionary are storing a value with some key and 
extracting the value given the key. 

## 3.1 Creating and storing data

A pair of braces creates an empty dictionary: `{}`. A colon `:` separates each key from its associated value:

### Syntax:

```python
my_dict = {"key": "value"}
```

Pairs in the dictionary are separated by commas `,`:

### Example:

```python
user_credentials = {"username": "test_user", "password": "securepassword123"}
```

The `dict()` constructor builds dictionaries directly from sequences of key-value pairs:

```python
my_dict = dict([("test_one", 1), ("test_two", 2), ("test_three", 3)])
```

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

```python
my_dict = dict(test_one=1, test_two=2, test_three=3)
```

## 3.2 Extracting values

Dictionary values can be accessed by a key:

### Syntax:

```python
d[key]
```
Return the value of the dictionary`d` with the key `key`. Raises a `KeyError` if `key` is not in the `d`.

### Example:

```python
test_one = my_dict["test_one"]
print(test_one)
```

```python
test_one = my_dict["test_1"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    test_one = my_dict["test_1"]
KeyError: 'test_1'
```

Use built-in function `get(key, default=None)` if it is required to return a default value if `key` is not in the `d`.
By default, `the get(key)` method returns `None`.

### Example:

```python
test_one = my_dict.get("test_1", 1)
print(test_one)
test_one = my_dict.get("test_1", 1)
print(test_one)
```

## 3.3 Updating values

The value can be updated also by a key:

### Syntax:

```python
d[key] = value
```
If there is no such key, it will be added to the `d`

### Example:

```python
my_dict["test_one"] = 0
print(my_dict)
my_dict["test_1"] = 1
print(my_dict)
```

## 3.4 Removing items

To remove a pair from the dictionary, use the `del` statement with an exact key to delete:

### Syntax:

```python
del d[key]
```
If there is no such key, it will raise `KeyError`

### Example:

```python
del my_dict["test_1"]
print(my_dict)
del my_dict["test_1"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    del my_dict["test_1"]
KeyError: 'test_1'
```

`pop(key, default)` method remove `key` from the dictionary and return its value. If `key` is not in 
the dictionary, it will return `defalt` if it is provided.


### Example:

```python
my_dict.pop("test_two")
my_dict.pop("test_two", "two")
my_dict.pop("test_two")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    my_dict.pop("test_two")
KeyError: 'test_two'
```

`popitem()`
Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order. If 
the dictionary is empty, calling `popitem()` raises a `KeyError`.

[NOTE] *Changed in version 3.7:* LIFO order is now guaranteed. In prior versions, popitem() would return an arbitrary 
key/value pair.

`clear()`
Remove all items from the dictionary.

## 3.5 Extracting keys

Performing `list(d)` on a dictionary returns a list of all the keys used in the dictionary, in insertion order:

### Example:

```python
list(my_dict)
```

Use `sorted(d)` to return a sorted list of all the keys:

### Example:

```python
sorted(my_dict)
```

To check if a key is in the dictionary, use `in`:

### Example:

```python
'test_three' in my_dict
```

## 3.6 Looping

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the `items()`
method.

### Example:

```python
for k, v in my_dict.items():
    print(k, v)
```

The `keys()` method returns a dict_keys object which contains keys from a dictionary and the `values()` method returns 
dict_values object with values of a dictionary. Both these objects are sequence objects:

### Example:

```python
for k in my_dict.keys():
    print(k)
```

```python
for v in my_dict.values():
    print(v)
```

## 3. Dictionary comprehension

A compact way to process all or part of the elements in an iterable and return a dictionary with the results.

In an example below we will generate a dictionary containing key n mapped to value n ** 2:

### Example:

```python
results = {n: n ** 2 for n in range(10)}
```

### Practical Exercises (Drills):
1. [TI] How can you merge two dictionaries in Python?
2. [TI] Is it possible to use a tuple as a key in the dictionary?
3. Write a function that takes a dictionary and returns a list of all the keys.
4. Created a nested dictionary.

 [Note] For the next two questions please refer to the previous lesson where you study Lists. Copying mechanism was 
explained there.

5. Create a shallow copy of a nested dictionary. Modify the original dictionary. How has the shallow copy changed?
6. Create a deep copy of a nested dictionary. Modify the original dictionary. How has the deep copy changed?
7. Write a function that inverts a dictionary (i.e., the keys become values and the values become keys).
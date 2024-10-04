# Section 4: Sets

A `set` is an `unordered` and `unindexed` collection of `unique` elements. They are useful when you need to eliminate `duplicates`, perform set operations like `unions`, `intersections`, and `differences`, and ensure that each element appears only once. Sets are `mutable`, but the elements themselves must be `immutable`.


## References:

- [Python Official Documentation on Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Real Python - Python Sets: A Detailed Guide](https://realpython.com/python-sets/)
- [W3Schools - Python Set](https://www.w3schools.com/python/python_sets.asp)

---


## 4.1 Creating

To create a `set` in Python, you can either define it with curly braces `{}` containing elements or use the `set()` function for an empty `set` or when initializing from an iterable.


### Syntax:

```python
my_set = {immutable_element_1, immutable_element_2, immutable_element_3}
```


### Example:

```python
# Creating a set
test_results = {'pass', 'fail', 'error', 'pass'} # Output: {'pass', 'error', 'fail'}

# Creating an empty set
empty_set = set() # Output: set()
```


## 4.2 Reading

Reading elements in a `set` is typically done through iteration. Since sets are `unordered`,  you cannot access elements by `index`.


### Using `in`:

`in` checks for membership.

```python
colors = {'red', 'blue', 'green'}

# Reading elements in a set
if 'blue' in colors:
    print('Blue is present in the set')

# Iterating over a set
for color in colors:
    print(color)

print(colors[0])  # Raises TypeError: 'set' object is not subscriptable
```


### Using `len()`

`len()` returns the number of elements in a set.

```python
my_set = {1, 2, 3}
len(my_set)  # 3
```


## 4.3 Updating

You can use the `add()` and `update()` methods to add elements to a `set`.


### `add()`:

It only adds a single element to a `set`. Adding existing element will be ignored

```python
colors = {'red', 'blue', 'green'}
colors.add('yellow')  # `colors` now is {'red', 'blue', 'yellow', 'green'}

# Adding an existing element will be ignored
colors.add('yellow')  # `colors` now is {'red', 'blue', 'yellow', 'green'}
```


### `update()`

It adds multiple elements. Adding existing elements will be ignored

```python
colors = {'red', 'blue', 'green', 'yellow'}
colors.update(['pink', 'black', 'red', 'yellow']) # `colors` now is {'yellow', 'pink', 'green', 'black', 'red', 'blue'}
```


### Shallow copy

Use `copy()` to create a shallow copy of a set.

```python
test_cases = {'TC01', 'TC02', 'TC03'}
shallow_copy_of_test_cases = test_cases.copy()
test_cases.add('TC04')
shallow_copy_of_test_cases.add('TC05')
print(test_cases) # Output: {'TC04', 'TC02', 'TC03', 'TC01'}
print(shallow_copy_of_test_cases) # Output: {'TC05', 'TC02', 'TC03', 'TC01'}
```


## 4.4 Deleting

You can remove elements from a `set` using `remove()`, `discard()`, `pop()` and `clear()` methods. Be cautious with `remove()` as it raises an error if the element is not found, whereas `discard()` will not.


### `remove()`:

Removes the specified element, but raises an error if it’s not found.

```python
colors = {'yellow', 'pink', 'green', 'black', 'red', 'blue'}
colors.remove('red') # `colors` now is {'yellow', 'pink', 'green', 'black', 'blue'}
colors.remove('red')  # It raises an exception similar to below

"""
Traceback (most recent call last):
  File "C:\python\py311\Lib\code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
KeyError: 'red'
"""
```


### `discard()`:

Removes the specified element, but does not raise an error if the element is not found.

```python
colors = {'yellow', 'pink', 'green', 'black', 'red', 'blue'}
colors.discard('black') # `colors` now is {'green', 'pink', 'red', 'blue', 'yellow'}
colors.discard('black') # Does nothing, no error

```

### `pop()`

Removes and returns an arbitrary element from the set.

```python
colors = {'green', 'pink', 'red', 'blue', 'yellow'}
value_returned = colors.pop() # Removes and returns an arbitrary element
print(value_returned) # Output: 'yellow'
```


### `clear()`

Removes all elements from the set.

```python
colors = {'green', 'pink', 'red', 'blue', 'yellow'}
colors.clear() # Removes and returns an arbitrary element
print(colors) # Output: set()
```


### Mathematical set operations:

Python sets support mathematical operations like `union`, `intersection`, `difference`, and `symmetric difference`, which are very efficient and commonly used in problem-solving.


#### Union:

Combines all unique elements from two or more sets.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.union(set_b) # Output: {1, 2, 3, 4, 5, 6}
```


#### Intersection:

Finds the common elements between sets.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.intersection(set_b) # Output: {3, 4}
```


#### Difference

Returns elements that are in the first `set` but not in the second.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.difference(set_b) # Output: {1, 2}
```

#### Symmetric Difference

Returns elements that are in either `set` but not in both.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_a.symmetric_difference(set_b) # Output: {1, 2, 5, 6}
```


#### Additional Set Methods


##### `intersection_update()`

Updates the first `set` to keep only elements found in both sets.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Only returns the common elements
set_a.intersection(set_b) # Output: {3, 4}
print(set_a) # Output: {1, 2, 3, 4}
print(set_b) # Output: {3, 4, 5, 6}

# The first set (also called `left` set) is updated with the common elements
set_a.intersection_update(set_b) # There is no output
print(set_a) # Output: {3, 4}
print(set_b) # Output: {3, 4, 5, 6}
```


##### `isdisjoint()`

Returns `True` if the sets have no elements in common, `False` if it has elements in common.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {7, 8, 9, 0}
set_a.isdisjoint(set_b) # Output: False
set_a.isdisjoint(set_c) # Output: True
```


##### `issubset()`

Checks if the `set` is a `subset` of another. A `subset` relationship requires that `all` elements of the first set must be present in the second set.

```python
set_a = {3, 4}
set_b = {3, 4, 5, 6}
set_a.isdisjoint(set_b) # Output: True. All elements in `set_a` are present in `set_b`
set_b.isdisjoint(set_a) # Output: False. Not all elements in `set_b` (5 and 6) are present in `set_a`
```


##### `issuperset()`

Checks if the `set` is a `superset` of another. A `superset` relationship means that one `set` must fully contain all elements of the other `set`.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4}
set_a.issuperset(set_b) # Output: True. All elements in `set_b` are present in `set_a`
set_b.issuperset(set_a) # Output: False. Not all elements in `set_a` (1 and 2) are present in `set_b`.
```


## Practical Exercises (Drills):

1. [TI] What are the main differences between Sets and Tuples?
2. [TI] What are the main differences between Sets and Lists?
3. [TI] Can we add a list of immutable elements to a `set`? Why?
4. [TI] Can we use a `set` as a key in a dictionary? Why?
5. Create a `set` with the numbers 1 through 5. Add the number 6 to the `set` and then update the `set` with numbers 7, 8, and 9.
6. Create two sets: `{1, 2, 3, 4}` and `{3, 4, 5, 6}`. Perform `union`, `intersection`, and `difference` on these sets.
7. Write a function that takes a list with duplicates and returns a list with unique elements by converting it into a `set`.
8. Write a function that takes two lists and returns a set of elements common to both lists.
9. [TI] Given a list of integers, write a function to determine how many elements from this list appear in a predefined `set` of even numbers `{2, 4, 6, 8, 10}`.

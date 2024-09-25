# Section 1: Lists

In this section, we will explore lists, one of the most commonly used data structures in Python.

Lists are `mutable` and `ordered` sequences that can store collections of items. They allow to have same values in them (duplicates) and allow for a range of operations, making them versatile for test automation.

We'll focus on how to `CRUD` (Create, Read, Update, and Delete) elements in lists, with practical examples relevant to test automation.


## References

1. [Lists - Python Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)
2. [More on Lists - Python Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
3. [Python Software Foundation list methods](https://docs.python.org/3/library/stdtypes.html#list)
4. [Python Lists - Real Python](https://realpython.com/python-lists-tuples/)
5. [Python Lists - W3Schools](https://www.w3schools.com/python/python_lists.asp)


---

## 1.1 Creating

In test automation, lists are used to store test data, such as input values or expected outputs. You can create a list using square brackets `[]`.


### Syntax:

Creating an empty list:

```python
variables = []
```

Creating a list with initial values:

```python
variables = ["Login", "Submit", "Logout"]
```

Creating a list using the `list()` constructor:

```python
digits = list() # creates an empty list
```

```python
digits = list(range(10)) # creates a list with: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Note:** Variables that represent sequences usually are named using plural.


### Examples:

```python
test_cases = [] # An empty list
test_cases = [1, 2, 3] # A list of numbers
test_cases = ["1", "2", "3"] # A list of strings
test_cases = ["Cat", 2] # A list of different data types
test_cases = ["Login Page", "Dashboard", "Logout Functionality"]
```

### Adding new elements

The `create` process for lists also involves `adding` new elements to a list. In Python, this can be done using various methods, but the most common one is `append()`, which allows you to add a new item to the end of a list. This is especially useful in test automation for dynamically building up test data during the execution of a test suite.

#### Syntax

The `append()` always adds a single element to the end of an existing list.

```python
list_name.append(element)
```


#### Example:

```python
test_cases = ['Login Test', 'Signup Test']
test_cases.append('Logout Test')
print(test_cases)  # Output: ['Login Test', 'Signup Test', 'Logout Test']
```


## 1.2 Reading

Reading from a list is essential for retrieving test data. Python allows reading individual elements or slices (subsets) of a list.

List are indexed by integers starting from 0. There is no size limit other than the memory capacity of the computer.  


### Syntax:

Reading elements by index:

```python
test_data[0]  # First element
test_data[1]  # Second element
test_data[-1]  # Last element
test_data[-2]  # Before last element
```


### Using the `len()` function for lists

The `len()` function in Python is used to determine the number of elements in a list. In test automation, the size of your test data is important for several reasons:
- `Validation`: You can use `len()` to verify that a function returns the expected number of results.
- `Boundary Conditions`: Understanding the size of a list helps in writing tests for edge cases like `empty` lists, `single-element` lists, and `large` lists.
- `Iteration`: The length of a list is often used in loops to iterate through all elements.


#### Syntax:

```python
list_length = len(my_list)
```


#### Example:

```python
test_cases = ['Login Test', 'Signup Test', 'Logout Test']
print(len(test_cases))  # Output: 3

nested_list = [[1, 2, 3], [4, 5], [6]] # The len() function counts only the top-level elements in a list, not the total number of elements within nested lists.
print(len(nested_list))  # Output: 3

empty_list = []
print(len(empty_list))  # Output: 0
```


### Slicing list:

When it comes to reading or accessing data in lists, slicing is a powerful technique in Python. Slicing allows you to extract a part of the list, whether it's a single element, a range, or a set of elements with a specific step.


#### Syntax:

```python
the_list_variable[start:stop:step]
```

- `start`: The starting index (inclusive). Defaults to 0 if not provided.
- `end`: The stopping index (exclusive). Defaults to the length of the list.
- `step`: **Optional** step between elements. Defaults to 1.


#### Examples:

**Default values in slicing**:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
slice_all = numbers[:]  # Same as copying the entire list
print(slice_all)  # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

**Basic slicing**:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_three = numbers[:3]
print(first_three)  # Output: [10, 20, 30]
```

**Slicing with steps**. The step parameter allows you to slice with strides, or intervals. This is useful for selecting every nth item or iterating through the list in reverse order:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
every_second = numbers[::2]
print(every_second)  # Output: [10, 30, 50, 70, 90]
```

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
only_third_and_fifth_elements = numbers[2:5:2]
print(only_third_and_fifth_elements)  # Output: [30, 50]
```

**Reverse a list**:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
reversed_list = numbers[::-1] # starts slicing from the last-to-first element
print(reversed_list)  # Output: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
```

**Negative indexing with slicing**. Python allows negative indexing, which means you can slice from the end of the list rather than the start. This can be helpful when you want to access elements relative to the end of a sequence:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
last_two = numbers[-2:] # starts slicing from the second-to-last element
print(last_two)  # Output: [90, 100]
```

**Modifying the original list with slices**. You can use slicing to update a subset of elements in a list. This can be quite useful when dealing with test data that needs to be updated in place:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers[1:3] = [100, 200]  # Replaces the second and third elements
print(numbers)  # Output: [10, 100, 200, 40, 50, 60, 70, 80, 90, 100]
```

**Copying a List with Slicing**. A common trick to create a shallow copy of a list is to use slicing. This is especially useful when you want to avoid modifying the original list in your test scripts:

```python
original = [1, 2, 3]
copy = original[:]
copy.append(4)
print(original)  # Output: [1, 2, 3]
print(copy)      # Output: [1, 2, 3, 4]
```

**Empty Slices**. If the `start` index is equal to or greater than the `end` index, the result is an empty list. This can be used as a `boundary condition` in tests:

```python
numbers = [10, 20, 30, 40, 50]
empty = numbers[4:2]  # Start index is greater than end index
print(empty)  # Output: []
```

**Out-of-Bounds Indexing**. If you specify an index that's beyond the length of the list, Python won't raise an `IndexError`. It will simply stop at the end of the list:

```python
numbers = [10, 20, 30, 40, 50]
out_of_bounds = numbers[2:10]
print(out_of_bounds)  # Output: [30, 40, 50]
```


## 1.3 Updating

Updating a list is useful when test data or test scenarios increase/decrease (evolve). You can modify elements by assigning new values to specific indexes.


### Syntax:

```python
# Updating the value of an element
test_cases[0] = "New Value"
```

### Adding elements to a list

As the `append()` method, that add a new element in a list, there are a few other ways.

#### extend(iterable)

The `extend()` method also adds items to the end of a list. However, the argument is expected to be an `iterable` like another list. The items in the input iterable are added as individual values:

```python
test_cases = ['Login Test']
test_cases.extend(['Signup Test', 'Logout Test']) # Output: ['Login Test', 'Signup Test', 'Logout Test']
```

This same behaviour is expected from the concatenation operator `+`.

```python
test_cases = ['Login Test']
test_cases = test_cases + ['Signup Test', 'Logout Test'] # Output: ['Login Test', 'Signup Test', 'Logout Test']
```


#### insert(index, obj)

The `insert()` method inserts the input object into the target list at the position specified by index. Following the method call, a[<index>] is <obj>, and the remaining list elements are pushed to the right:

## Hands-On Task:

1. Create a list of numbers and extract every second number from it.
2. Reverse a list using slicing and verify if the list has been reversed correctly.
3. Use slicing to reverse a list, modify a subset of it, and then restore the original list using a copy.
4. Extract a sublist from index 1 to 3 from a list of test case IDs.
5. Slice a list with a step of 3 to get every third element, starting from the second position.
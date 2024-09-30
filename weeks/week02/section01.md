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

**Note:** It's a good practice to use plural names for lists to indicate they hold multiple items.


### Examples:

```python
test_cases = [] # An empty list
test_cases = [1, 2, 3] # A list of numbers
test_cases = ["Login Page", "Dashboard", "Logout Functionality"] # A list of strings
test_cases = ["Login Page", 2, True] # A list of different data types

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


#### List Comprhensions:

List comprehensions offer a concise way to create lists. They allow you to generate new lists by applying an expression to each element in an iterable.

##### Syntax:

```python
[expression for item in iterable if condition]
```

##### Example:

- Creating a list of squared numbers from an existing list:

    ```python
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(squares)  # Output: [1, 4, 9, 16, 25]
    ```

- Creating a list of only even numbers:
    
    ```python
    even_numbers = [n for n in range(10) if n % 2 == 0]
    print(even_numbers)  # Output: [0, 2, 4, 6, 8]
    ```


#### Copying Lists:

Copying lists can be tricky in Python, especially if it's a nested or complex list. Simply using `=` to copy a list only creates a reference to the original list, not an actual copy. This can cause issues in test automation if changes to one list affect another.

##### Example:

```python
test_cases = ['Login', 'Signup', 'Logout']
test_cases_copy = test_cases  # This is a reference, not a copy
test_cases_copy.append('Dashboard')
print(test_cases)  # Output: ['Login', 'Signup', 'Logout', 'Dashboard']
```

The proper ways to copy a list can be using `list()` or the `copy()` method

```python
test_cases = ['Login', 'Signup', 'Logout']
test_cases_copy = list(test_cases)
test_cases_copy.append('Dashboard')
print(test_cases)  # Output: ['Login', 'Signup', 'Logout']
print(test_cases_copy)  # Output: ['Login', 'Signup', 'Logout', 'Dashboard']
```

```python
test_cases = ['Login', 'Signup', 'Logout']
test_cases_copy = test_cases.copy()
test_cases_copy.append('Dashboard')
print(test_cases)  # Output: ['Login', 'Signup', 'Logout']
print(test_cases_copy)  # Output: ['Login', 'Signup', 'Logout', 'Dashboard']
```

**Note:** Using these ways are also called as `Shallow Copy`. This means that only the `outer` list is copied, but the `inner` lists remain references to the original ones. Changes to the inner lists will affect both the original and copied lists.

```python
import copy # built-in library to support copy mechanisms

# Original list with nested lists
original_list = [['Login', 'Signup'], ['Logout', 'Settings']]

# Shallow copy of the list
shallow_copy = original_list.copy()

# Modifying an inner list in the shallow copy
shallow_copy[0].append('Dashboard')

# Both the original and shallow copy are affected
print("Original List:", original_list)  # Output: [['Login', 'Signup', 'Dashboard'], ['Logout', 'Settings']]
print("Shallow Copy:", shallow_copy)    # Output: [['Login', 'Signup', 'Dashboard'], ['Logout', 'Settings']]
```

We should use `Deep Copy` to avoid referencing issues. It creates a completely independent copy of both the `outer` and `inner` lists, ensuring no references are shared between the two.

```python
import copy

# Original list with nested lists
original_list = [['Login', 'Signup'], ['Logout', 'Settings']]

# Deep copy of the list
deep_copy = copy.deepcopy(original_list)

# Modifying an inner list in the deep copy
deep_copy[0].append('Dashboard')

# The original list remains unchanged
print("Original List:", original_list)  # Output: [['Login', 'Signup'], ['Logout', 'Settings']]
print("Deep Copy:", deep_copy)          # Output: [['Login', 'Signup', 'Dashboard'], ['Logout', 'Settings']]
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

Updating a list is useful when test data or test scenarios increase/decrease (evolve). You can update a list by modifying its elements, appending new items, or even inserting elements at specific positions.


### Syntax:

```python
# Updating the value of an element
test_cases[0] = "New Value"
```


### Adding elements to a list

While append() adds a single element to the end of a list, other methods provide more flexibility.


#### extend(iterable)

The `extend()` method also adds items to the end of a list. However, the argument is expected to be an `iterable` like another list. The items in the input iterable are added as individual values:

```python
test_cases = ['Login Test']
test_cases.extend(['Signup Test', 'Logout Test']) # Output: ['Login Test', 'Signup Test', 'Logout Test']
print(test_cases) # Output: ['Login Test', 'Signup Test', 'Logout Test']
```

This is equivalent to using the `+` operator:

```python
test_cases = ['Login Test']
test_cases = test_cases + ['Signup Test', 'Logout Test'] # Output: ['Login Test', 'Signup Test', 'Logout Test']
```


#### insert(index, obj)

The `insert()` method adds an element at a specific index, pushing the other elements to the right:

- Add at the beginning:

    ```python
    test_cases_id = ['TC01', 'TC02', 'TC03', 'TC04']
    test_cases_id.insert(0, 'TC00')
    print(test_cases_id) # Output: ['TC00', 'TC01', 'TC02', 'TC03', 'TC04']
    ```

- Add at the end:

    ```python
    test_cases_id = ['TC01', 'TC02', 'TC03', 'TC04']
    test_cases_id.insert(len(test_cases_id), 'TC05') # This is equivalent to test_cases_id.append('TC05')
    print(test_cases_id) # Output: ['TC01', 'TC02', 'TC03', 'TC04', 'TC05']
    ```

- Add at the middle:

    ```python
    test_cases_id = ['TC01', 'TC02', 'TC03', 'TC04']
    test_cases_id.insert(2, 'TC02.1')
    print(test_cases_id) # Output: ['TC01', 'TC02', 'TC02.1', 'TC03', 'TC04']
    ```


#### List Comprehensions for Updating:

List comprehensions can also be used to update lists by transforming existing elements or creating a modified copy of the original list.


##### Example:

- Updating all test cases to add a "Test" suffix:

    ```python
    test_cases = ["Login", "Signup", "Logout"]
    updated_cases = [case + " Test" for case in test_cases]
    print(updated_cases)  # Output: ['Login Test', 'Signup Test', 'Logout Test']
    ```

- Replacing all numbers with their squared values:

    ```python
    numbers = [1, 2, 3, 4]
    print(numbers)  # Output: [1, 2, 3, 4]
    numbers = [n**2 for n in numbers]
    print(numbers)  # Output: [1, 4, 9, 16]
    ```


## 1.3 Deleting

In test automation, there are situations where test data needs to be dynamically removed from lists. Python provides several ways to delete elements from a list, each serving different use cases.


### `pop(index)`:

The `pop()` method removes an element at the specified index and returns the element. If no index is provided, it removes and returns the `last item` of the list. This is particularly useful when you need to remove an element while preserving it for later use.


#### Syntax:

```python
list_name.pop(index)
```


#### Example:

```python
test_cases = ['Login', 'Signup', 'Logout']

# Removing the last element
last_case = test_cases.pop()
print(test_cases)  # Output: ['Login', 'Signup']
print(last_case)   # Output: 'Logout'

# Removing the first element by index
first_case = test_cases.pop(0)  
print(test_cases)  # Output: ['Signup']
print(first_case)  # Output: 'Login'
```


### `remove(element)`:

The `remove()` method removes the first occurrence of the specified element. It `does not return` the removed element. This method is useful when you want to delete an item based on its value rather than its position.


#### Syntax:

```python
list_name.remove(element_value)
```


#### Example:

```python
test_cases = ['Login', 'Signup', 'Logout', 'Signup']

# Removing the first occurrence of 'Signup'
test_cases.remove('Signup')
print(test_cases)  # Output: ['Login', 'Logout', 'Signup']
```

**Note:** If the element is not found in the list, a `ValueError` is raised. You can handle this with `try` and `except` if needed.


### `del` statement:

The `del` statement allows you to delete elements by index. Unlike `pop()`, it `does not return` the removed element. It is also capable of deleting multiple elements at once by `slicing` or `deleting` the entire list.


#### Syntax:

```python
del list_name[index] # Deletes the element at the specified index
del list_name # Deletes the entire list
```


#### Example:

```python
test_cases = ['Login', 'Signup', 'Logout', 'Settings']

# Deleting an element by index
del test_cases[1]
print(test_cases)  # Output: ['Login', 'Logout', 'Settings']

# Deleting multiple elements using slicing
del test_cases[1:3]
print(test_cases)  # Output: ['Login']

# Deleting the entire list
del test_cases
```

**Note:** After using `del test_cases`, the list no longer exists, and any further reference to it will result in a `NameError` exception.


### `clear()`:

The `clear()` method removes all elements from the list, but keeps the list itself intact. This is helpful when you need to reset a list without deleting the actual list object.


#### Example:

```python
test_cases = ['Login', 'Signup', 'Logout']

# Clearing the list
test_cases.clear()
print(test_cases)  # Output: []
```


## Hands-On Task:

1. [TI] What are the main characteristics/properties of Lists in Python?
2. Create a list of numbers and extract every second number from it.
3. Reverse a list using slicing and verify visually if the list has been reversed correctly.
4. Use slicing to reverse a list, modify a subset of it, and then restore the original list using a copy.
5. Extract a sublist from index 1 to 3 from a list of test case IDs.
6. Slice a list with a step of 3 to get every third element, starting from the second position.
7. Add 3 new elements to the end of a list using different methods (`append()`, `extend()`, and `insert()`).
8. Remove the second element from a list using the `pop()` method and print the removed element.
9. Remove the first occurrence of a specific value from a list using the `remove()` method.
10. Clear a list and then add elements back to it using `append()` inside a loop.
11. Create a shallow copy of a list containing nested lists and modify one of the inner lists. Observe how the original list changes.
12. Create a deep copy of a list using `copy.deepcopy()` from the `copy` module and modify one of the inner lists. Verify that the original list remains unchanged.
13. Create a list comprehension to generate a list of squared numbers from 1 to 10.
14. Use list comprehension to create a new list with only the even numbers from an existing list.

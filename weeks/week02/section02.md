# Section 2: Tuples

In this section, we will explore tuples, another core data structure in Python.

`Tuple` is a type of data structure that is similar to lists. The main difference between the two is that tuples are `immutable`, meaning they cannot be changed after creating. Here a list of characteristics about Tuples:

- Tuples are `immutables`, can't be changed.
- Used to store collections of heterogeneous data (any type of data: string, boolean, etc)
- Rounded by parenthesis `()`
- Only two built-in method:
  - `count()`: Returns the number of times a specified value occurs in a tuple
  - `index()`: Searches the tuple for a specified value and returns the position of where it was found
- Uses `less memory` and is `faster` to access to elements when comparing with `lists`


## References:

1. [Tuples and Sequences - Python Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
2. [Lists vs Tuples in Python - Real Python](https://realpython.com/python-tuples/)
3. [Python Tuples - W3Schools](https://www.w3schools.com/python/python_tuples.asp)
4. [Python Tuples - GeeksForGeeks](https://www.geeksforgeeks.org/python-tuples/)

---


## 2.1 Creating

Tuples are useful in test automation for storing `immutable` collections of test data, such as constant values or configuration parameters. Tuples can be created values separated by commas, using parentheses `()` or the `tuple()` constructor.


### Syntax:

```python
# Using values separated by commas
test_tuple = value, value, value

# using parenthesis
test_tuple = () # empty tuple
test_tuple = (value1,)
test_tuple2 = (value1, value2)

# from contructor:
test_from_constructor = tuple() # empty tuple

# from list
tuple_from_list = tuple([11, 22, 33])

# from any sequence of elements (e.g. range)
tuple_from_range = tuple(range(10))
```


### Example:

```python
test_cases = ()  # An empty tuple
test_cases = (1, 2, 3)  # A tuple of numbers
test_cases = ("Login Page", "Dashboard", "Logout Functionality")  # A tuple of strings
test_cases = ("Login Page", 2, True)  # A tuple of different data types
```

**Note:** Even though tuples are immutable, they can contain mutable objects like lists. However, the tuple itself cannot be modified after creation.


## 2.2 Reading

2.2.1
Tuples are indexed in the same way as lists, meaning each element in the tuple can be accessed by its index. The index starts at 0, and negative indexing is also supported.


### Syntax:

```python
test_data[0]  # First element
test_data[1]  # Second element
test_data[-1]  # Last element
test_data[-2]  # Second-to-last element
```
2.2.2 Extract/ Unpack/ Assigning to variables
Tuples elements can be assigned to variable (unpacked / extracted as follow)

```python
max_spead = (12, 30, 60)

(first_gear, second_gear, third_gear) = max_spead
or
one, two, three = max_spead
*Remark* There is good practice use name "_" if value is not needed
_, two, three = max_spead


print(first_gear)  # output 12
print(second_gear)  # output 30
print(third_gear)  # output 60
print(two)  # output 30
```
The reference link: [Python Tuples - W3Schools](https://www.w3schools.com/python/python_tuples_unpack.asp)

### Using the `len()` function for tuples:

Just like with lists, the `len()` function is used to find the number of elements in a tuple.


#### Example:

```python
test_cases = ("Login Test", "Signup Test", "Logout Test")
print(len(test_cases))  # Output: 3

nested_tuple = ((1, 2, 3), (4, 5), (6,))
print(len(nested_tuple))  # Output: 3
```


### Slicing Tuples:

Tuples support `slicing`, similar to lists. Slicing allows extracting parts of a tuple without modifying the original data.


#### Syntax:

```python
tuple_variable[start:stop:step]
```


#### Examples:

- Basic slicing:

```python
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
first_three = numbers[:3]
print(first_three)  # Output: (10, 20, 30)
```

- Slicing with steps:

```python
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
every_second = numbers[::2]
print(every_second)  # Output: (10, 30, 50, 70, 90)
```

- Negative slicing

```python
numbers = (10, 20, 30, 40, 50)
last_two = numbers[-2:]
print(last_two)  # Output: (40, 50)
```

- Revert a tuple:

```python
numbers = (10, 20, 30, 40, 50)
reverted_tuple = numbers[::-1]
print(reverted_tuple)  # Output: (50, 40, 30, 20, 10)
```


- Out-of-Bounds indexing

```python
numbers = (10, 20, 30)
out_of_bounds = numbers[2:10]
print(out_of_bounds)  # Output: (30,)
```


## 2.3 Updating

Tuples are `immutable`, meaning they cannot be changed once created. You `cannot` update the elements of a tuple after it has been defined. With that said, there is a workaround for "updating" a tuple.

If you need to "update" a tuple, you can convert it into a list, make the necessary changes, and then convert it back into a tuple. This is common in test automation when dealing with static test data that may need minor adjustments.


### Example:

```python
test_data = ("Login", "Signup", "Logout")

# Convert tuple to list
test_data_list = list(test_data)
test_data_list[0] = "Login Test"  # Update the first element

# Convert back to tuple
test_data = tuple(test_data_list)
print(test_data)  # Output: ('Login Test', 'Signup', 'Logout')
```


## 2.4 Deleting

Tuples, being immutable, cannot have their elements deleted directly. However, you can delete the entire tuple using `del` statement.

### Syntax:

```python
del tuple_name
```



## Practical Exercises (Drills):

1. Create a tuple containing multiple types of elements, including an integer, a boolean, a list, another tuple, and a string.
2. Print the data type of the third element in the tuple you created in the previous exercise. Tip: use [type()](https://www.programiz.com/python-programming/methods/built-in/type) or [isinstance()](https://www.programiz.com/python-programming/methods/built-in/isinstance)` method.
3. Explain why you cannot directly add a new element to a tuple. Then, demonstrate how to create a new tuple that includes an additional element.
4. Create a tuple called tuple_to_sort with the elements (2, 6, 4, 17, 9, 3, 15, 7). Write code to return a new tuple that contains the sorted elements of this tuple.
5. Using the tuple_to_sort from the previous exercise, write code to create a new tuple that contains the two largest elements.
6. Create a tuple with repeated elements (e.g., (1, 2, 3, 2, 4, 1, 5)) and write a function to count the occurrences of each unique element in the tuple.
7. Convert the tuple you created in Exercise 1 into a list and print the result. Discuss why you might want to convert a tuple to a list.
8. Write code to check if a specific value (e.g., True or 4) is present in the tuple you created in Exercise 1. Print the result.
9. Write code to slice the tuple from Exercise 1 and return the second and third elements.
10. If your original tuple contains another tuple, demonstrate how to access an element from the nested tuple.

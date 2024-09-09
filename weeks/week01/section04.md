# Section 4: Functions

Functions are reusable blocks of code that perform specific tasks. Python provides a wide range of built-in functions, as well as the ability to define your own custom functions. In this section, we'll cover how to use some essential built-in functions such as `input()`, `print()`, casting functions, and others.


## 4.1 Built-in Functions

Python provides several built-in functions that simplify common tasks, such as getting user input, printing output, and converting data types. These functions are crucial for creating interactive test scripts and handling test data.


### 4.1.1 `input()`

The `input()` function allows you to capture user input from the console. This is especially useful in test automation scripts where you might want to input test data manually.
   ```python
   # Capturing user input for a test case
   username = input("Enter your username: ")
   ```

**`Note`**: By default, `input()` returns a string, so you might need to cast the input to another data type if necessary.


### 4.1.2 `print()`
The `print()` function is used to output data to the console. This is one of the most commonly used functions in Python for debugging and displaying test results.
   ```python
   # Printing test results
   test_passed = True
   print("Test passed:", test_passed)
   ```

You can also use formatted strings (`f-strings`) to embed variables inside your output:

   ```python
   # Using f-strings for formatted output
   username = "test_user"
   print(f"Welcome, {username}!")
   ```


### 4.1.3 Casting Functions
Casting functions convert data from one type to another. These are essential when working with input or when manipulating data for tests.
- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a floating-point number.
- `str()`: Converts a value to a string.
- `bool()`: Converts a value to a boolean.

   ```python
   # Converting a string to an integer
   age_str = "25"
   age = int(age_str)
   
   # Converting a float to an integer
   price_float = 19.99
   price_int = int(price_float)
   
   # Converting an integer to a string
   test_count = 5
   test_count_str = str(test_count)
   
   # Converting to a boolean
   is_active = bool(1)  # True
   ```

### Hands-On Task:
Write a script that:
- Asks for the user's age using input().
- Converts the input to an integer using int().
- Prints whether the user is an adult (age >= 18) using print().

## 4.2 Defining Your Own Functions
In Python, you can define your own functions using the `def` keyword. Functions can take inputs (called parameters) and return outputs (using the `return` statement). This is useful for organizing test scripts and reusing code.

   ```python
   # Defining a function to calculate test pass percentage
   def calculate_pass_percentage(total_tests, failed_tests):
       passed_tests = total_tests - failed_tests
       return (passed_tests / total_tests) * 100
   
   # Using the function in a script
   total = 10
   failed = 2
   percentage = calculate_pass_percentage(total, failed)
   print(f"Pass percentage: {percentage}%")
   ```
### Hands-On Task:
Define a function that takes two numbers as input and returns their product. Call this function with different test data.


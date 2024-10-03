# Section 2: Python Basics

This section introduces the basic building blocks of Python: variables, data types, and operators. Understanding these are essential for writing test scripts as they allow you to manage test data, define test conditions, and perform calculations in tests.


## References:
1. [Python comments](https://www.w3schools.com/python/gloss_python_comments.asp)
2. [Python Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
3. [Python Data Types](https://docs.python.org/3/library/stdtypes.html)
4. [Python Operators](https://www.w3schools.com/python/python_operators.asp)
5. [Basic Data Types](https://realpython.com/python-data-types/)
6. [Python Operators](https://www.geeksforgeeks.org/python-operators/)

---


## 2.1 Comments

Comments are non-executable lines in your code used to describe or explain what the code does. They are essential in test automation scripts for providing context, making the script easier to maintain and understand by other testers or developers.


### Types of Comments:

- **`Single-line Comments`**: Start with a `#` symbol. They are often used to annotate specific lines of code.

  ```python
  # This is a single-line comment
  passed_tests = 3  # This variable stores the number of passed tests
  ```

- **`Multi-line Comments`**: Enclosed in triple quotes (''' or """). These are helpful for longer explanations or documentation at the start of a function or script.

  ```python
  '''
  This function calculates the number of passed tests
  and returns the percentage of tests that passed.
  '''
  def calculate_pass_percentage(total_tests, failed_tests):
    passed_tests = total_tests - failed_tests
    return (passed_tests / total_tests) * 100
  ```


### Best Practices:

- Use comments to explain why certain decisions are made in the code, not just what the code does.
- Keep comments concise and relevant to the code section.
- Avoid over-commenting on code that is self-explanatory.


### Hands-On Task:

Add comments to a script and run the code. Observe that they are not print out to the console.


## 2.2 Variables

Variables are placeholders used to store data that can be referenced and manipulated. In test automation, variables help you store test inputs, expected outputs, or results.


### Rules for Naming Variables:

- Variable names should be **descriptive** and reflect their purpose (e.g., `test_case_count`, `login_status`).
- Must start with a **letter** or an **underscore** (e.g., `_username`, `user_name`).
- Can contain letters, numbers, and underscores, but **cannot start with a number** (e.g., `username1` is valid, but `1username` is not).
- Variable names are **case-sensitive** (`UserName` and `username` are considered different).
- Avoid using Python **keywords** like `if`, `else`, `while`, etc., as variable names.


### Sintaxe:

   ```python
   variable_name = value
   ```


### Example:

   ```python
   # Storing user data for testing
   username = "test_user"
   password = "pass123"
   login_attempts = 3
   ```


### Hands-On Task:

Create variables to store test data, such as usernames, passwords, and expected outputs for tests.


## 2.2 Data Types

Python supports several data types, which are essential for organizing and manipulating test data. Let's check the main `built-in` types below (check the completed [list of types](https://docs.python.org/3/library/stdtypes.html#))

- [Text type](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str):
  - `str` (strings): Text data between single or double quotes, e.g., ```username = "test_user"```.
  - This is an immutable type.
  - To use a quote as a string, we need to use the other type of quote, e.g., ```text_with_quote = '"my quote"'```
- [Numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex):
  - `int`: Integer numbers without any kind of quotes, e.g., ```retry_count = 3```.
  - `float`: Floating-point numbers, using `.` for the decimal representation, e.g., ```test_duration = 0.5```.
  - `complex`: [Complex numbers](https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/) have their uses in many applications related to mathematics and python provides useful tools to handle and manipulate them.
- [Sequence types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range):
  - `list`: A mutable sequence of objects of any type. It uses square brackets to set a list and the items are separated by commas, e.g., ```test_inputs = [1, '1', '$']```
  - `tuple`: An immutable sequence of objects of any type. It uses parentheses to set a tuple and the items are separated by commas, e.g., ```test_inputs = (1, '1', '$')```
  - `range`: Represents an immutable sequence of numbers. The syntax is: `range(start, stop, step)`, e.g., ```range(1, 10, 2)```, ```range(10, 20)```, ```range(15)```.
- [Mapping type](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict):
  - `dict`: An unordered and mutable pair Key-Value for mapping objects.
  - `Keys` should be immutable types of objects.
  - Use a comma-separated list of `key: value` pairs within braces, e.g., ```{'jack': 4098, 'sjoerd': 4127}``` or ```{4098: 'jack', 4127: 'sjoerd'}```.
- [Set types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset):
  - `set`: An unordered and mutable collection of distinct objects of any type. It uses braces and commas to be represented. e.g., ```usernames = {"jack", "jonh"}```
  - `fronzenset`: It is similar to set, except that frozensets are immutable.
- [Boolean](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool):
  - `Booleans (bool)`: Keywords `True` or `False` values, e.g., ```is_test_passed = True```.
  - The numbers `0` and `1` are read as `False` and `True`, respectively.
  - An empty string (`''` or `""`) is read as `False`.
  - An empty collection (`[]` or `()` or `{}`) is read as `False`.


### Typing (type hints)

Python is dynamically typed. It means variable types are determined at runtime, not at the time of declaration. We don't need to declare the type of variable explicitly, and its type can change over the time. For example:

  ```python
  password = "pass123"
  password = 123456
  ```

Since Python 3.5, the [type hinting](https://docs.python.org/3/library/typing.html) functionality was added. This is a way to specify the expected types of variables, function arguments, and return values.

**`Note`**: The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.


#### Example:

   ```python
   def add(x: int, y: int) -> int:
       return x + y
   ```


#### Hands-On Task:

Write a script that initializes variables of different data types (strings, integers, booleans) to store test results and log information.


## 2.3 Operators

Python has several operators that allow you to perform calculations, comparisons, and logic operations. These operators are crucial in test conditions and validating outputs.


### Main Operators:

- Arithmetic Operators:

| Operator | Name           | Example         |
|----------|----------------|-----------------|
| `+`      | Addition       | 10 + 20 = 30    |
| `-`      | Subtraction    | 20 – 10 = 10    |
| `*`      | Multiplication | 10 * 20 = 200   |
| `/`      | Division       | 20 / 10 = 2     |
| `%`      | Modulus        | 22 % 10 = 2     |
| `**`     | Exponent       | 4**2 = 16       |
| `//`     | Floor Division | 9//2 = 4        |


- Comparison Operators:

| Operator | Name                     | Example              |
|----------|--------------------------|----------------------|
| `==`     | Equal                    | `4 == 5` is not true |
| `!=`     | Not Equal                | `4 != 5` is true     |
| `>`      | Great Than               | `4 > 5` is not true  |
| `<`      | Less Than                | `4 < 5` is true      |
| `>=`     | Greater than or Equal to | `4 >= 5` is not true |
| `<=`     | Less than or Equal to    | `4 <= 5` is true     |


- Logical Operators:

Let's assume `a = True` and `b = False`.

| Operator | Name                                                                     | Example                 |
|----------|--------------------------------------------------------------------------|-------------------------|
| `AND`    | If both of the operands are true then the condition becomes true.        | `(a and b)` is true     |
| `OR`     | If any of the two operands is non-zero then the condition becomes true.  | `(a or b)` is true      |
| `NOT`    | Used to reverse the logical state of its operand                         | `Not(a and b)` is false |


- Assignment Operators:

| Operator | Name                      | Example                          |
|----------|---------------------------|----------------------------------|
| `=`      | Assignment Operator       | `a = 10`                         |
| `+=`     | Addition Assignment       | `a += 5` (Same as `a = a + 5`)   |
| `-=`     | Subtraction Assignment    | `a -= 5` (Same as `a = a - 5`)   |
| `*=`     | Multiplication Assignment | `a *= 5` (Same as `a = a * 5`)   |
| `/=`     | Division Assignment       | `a /= 5` (Same as `a = a / 5`)   |
| `%=`     | Remainder Assignment      | `a %= 5` (Same as `a = a % 5`)   |
| `**=`    | Exponent Assignment       | `a **= 2` (Same as `a = a ** 2`) |
| `//=`    | Floor Division Assignment | `a //= 3` (Same as `a = a // 3`) |


- Membership Operators:

Let's assume `a = [1, 2, 3]`

| Operator | Name                                                                                            | Example                   |
|----------|-------------------------------------------------------------------------------------------------|---------------------------|
| `in`     | Evaluates to true if it finds a variable in the specified sequence and false otherwise.         | `1 in a` returns True     |
| `not in` | Evaluates to true if it does not find a variable in the specified sequence and false otherwise. | `5 not in a` returns true |


- Identy Operators:

Let's assume `a = 10` and `b = 5`.

| Operator | Name                                                                                                           | Example                   |
|----------|----------------------------------------------------------------------------------------------------------------|---------------------------|
| `is`     | Evaluates to true if the variables on either side of the operator point to the same object and false otherwise | `a is b` returns False    |
| `is not` | Evaluates to false if the variables on either side of the operator point to the same object and true otherwise | `a is not b` returns True |


### Practical Exercises (Drills):

1. Create variables for the following:
- username as a string.
- login_attempts as an integer.
- is_logged_in as a boolean.
- test_duration as a float representing the time (in seconds) it took for a test case to execute.

2. Identify the errors in the following variable names and correct them:
- 1user = "John"
- password length = 8
- is_valid? = True

3. Write a script that:
- Assigns a string, integer, float, and boolean to different variables.
- Prints each variable’s type using the `type()` function.

4. Write a script to calculate the percentage of tests passed. Given the total number of tests and the number of failed tests, calculate how many passed and what percentage of the total that represents.
- `total_tests = 100`
- `failed_tests = 5`
- `passed_tests = total_tests - failed_tests`
- `pass_percentage = (passed_tests / total_tests) * 100`

5. Go through your scripts from Exercises 1–4 and add comments explaining:
- What each variable represents.
- Why certain operations are performed.
- Use both `single-line` and `multi-line` comments where appropriate.

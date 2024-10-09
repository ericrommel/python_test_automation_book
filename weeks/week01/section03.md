# Section 3: Control Structures

Control structures are essential for decision-making in test scripts. In this section, you'll learn how to use `if-else` statements to handle different test cases and loops (`for` and `while`) to iterate over data sets or repeat actions in your scripts.


## References:

1. [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
2. [Python If-Else](https://www.w3schools.com/python/python_conditions.asp)
3. [For and While Loops](https://realpython.com/python-loops-iterators/)
4. [Python Control Structures](https://www.geeksforgeeks.org/decision-making-in-python/)
5. [Python Loops](https://www.programiz.com/python-programming/for-loop)

---


## 3.1 `if`, `elif`, and `else` Statements

The `if-elif-else` statements lets you make decisions in your code. In test automation, this can be used to determine if a test passes or fails based on the test result.


The `if` statement is used to execute a block of code only if a specified condition is true.


The `elif` (meaning `else if`) and `else` blocks provide additional conditional checks and a fallback when none of the conditions are true.


### Syntax:

   ```python
   if condition:
       # Code to execute if condition is true
   elif condition:
       #
   else:
       # Code to execute if condition is false
   ```


### Example:

   ```python
   def login(username):
       valid_user = "test_user"
       if username == valid_user:
           return "Login Successful"
       else:
           return "Login Failed"

   # Test cases
   print(login("test_user"))  # Should return "Login Successful"
   print(login("invalid_user"))  # Should return "Login Failed"

   ```


### Hands-On Task:

Write a script that checks whether a user’s score falls within certain ranges:
- If the score is 90 or above, print "Excellent".
- If the score is between 75 and 89, print "Good".
- If the score is between 50 and 74, check if the test was critical, and print "Critical test passed with average score" or "Non-critical test passed with average score".
- If the score is below 50, print "Fail".


## 3.2 Loops

Loops are used to execute a block of code multiple times, which is essential for running tests with different data sets.


### Syntax:

   ```python
   # While loop
   while condition:
       # Code to execute while condition is true

   # For loop
   for item in sequence:
       # Code to execute for each item in the sequence
   ```


### 3.2.1 `for` Loops

A `for` loop is used for iterating over a sequence (e.g., a list, tuple, dictionary, set, or string). You can use for loops to repeat an action for a specific number of iterations, which is useful when working with test cases or data sets.


#### Example:

   ```python
   # Looping over a list of test cases
   test_cases = ["Test1", "Test2", "Test3"]

   for test in test_cases:
       print(f"Running {test}")
   ```


#### Hands-On Task:

Write a for loop to iterate over a list of test scores and print whether each score represents a "Pass" or "Fail" (e.g., scores >= 50 are a pass).


### 3.2.2 `while` Loops

A while loop continues executing as long as the specified condition remains true. This is helpful when you don’t know in advance how many times the loop should run, such as waiting for a condition to be met in an automation task.


#### Example:

   ```python
   # Using a while loop to retry a test case until it passes
   test_passed = False
   attempts = 0

   while not test_passed and attempts < 3:
       print("Running test...")
       attempts += 1
       # Simulate test pass on 3rd attempt
       if attempts == 3:
           test_passed = True
           print("Test passed on attempt", attempts)
   ```


#### Hands-On Task:

Write a while loop that simulates retrying a test case up to 5 times until it passes. Use a condition to break out of the loop early if the test passes.


### 3.2.3 `break` and `continue` Statements

- `break`: Exits the loop entirely.
- `continue`: Skips the current iteration and moves to the next one.


#### Examples:

   ```python
   # Breaking out of a loop if a condition is met
   test_cases = ["Test1", "Test2", "Test3", "Test4"]

   for test in test_cases:
       if test == "Test3":
           print(f"{test} failed, stopping further tests.")
           break
       print(f"Running {test}")
   ```


#### Practical Exercises (Drills):

1. Create a script that uses arithmetic operators to calculate the percentage of passed and failed tests, then use comparison and logical operators to check if the tests meet a predefined success rate, given:
- Percentage of passed is calculated by dividing the number of passed tests by the total number of tests and then multiplying by 100.
- Percentage of failed is calculated by subtracting 100 by percentage of passed tests.
- To check if the percentage of passed tests meets the success rate threshold, just check if the percentage of passed is greater than or equals to a success rate threshold defined earlier.

2. Write a loop that iterates over test cases. If the current test case fails, break out of the loop; otherwise, print the result.

3. Write a script that checks if a user is eligible for a special test case discount:
- The user must be a registered tester and must have run at least 5 tests in the last week.
- If the user meets both conditions, print "Eligible for discount".
- If the user is registered but hasn’t run 5 tests, print "Not enough tests for discount".
- If the user is not registered, print "Not eligible for discount".

3. Create a list of test results (e.g., [True, False, True, False]). Write a `for` loop that prints `"Test Passed"` for `True` values and `"Test Failed"` for `False` values.

4. Simulate a test runner that will continue running test cases until all tests pass. If a critical test fails, stop the runner early using a `break` statement.

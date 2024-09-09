# Week 1: Python Basics, Control Structures, and Functions in Test Scripts

## Introduction

In this session, we will start by covering essential Python fundamentals, including **variables**, **data types**, and **operators**, which are critical for understanding how control structures and functions work in test scripts. We will also ensure all necessary tools are installed and set up.

### What You Will Learn:
- Python variables and data types.
- Main operators for calculations and comparisons.
- How to use control structures (if-else, loops) in test scripts.
- How to define and use functions to modularize and reuse test code.

---


### [Section 1](section01.md): Setting Up Tools

### [Section 2](section02.md): Python Basics

### [Section 3](section03.md): Control Structures

### [Section 4](section04.md): Functions

## Hands-On Exercises:
### Exercise 1: Variable Assignment

Create variables for the following:
- username as a string.
- login_attempts as an integer.
- is_logged_in as a boolean.
- test_duration as a float representing the time (in seconds) it took for a test case to execute.


### Exercise 2: Naming Variables

Identify the errors in the following variable names and correct them:
- 1user = "John"
- password length = 8
- is_valid? = True


### Exercise 3: Data Types Practice

Write a script that:
- Assigns a string, integer, float, and boolean to different variables.
- Prints each variable’s type using the type() function.


### Exercise 4: Simple Arithmetic

Write a script to calculate the percentage of tests passed. Given the total number of tests and the number of failed tests, calculate how many passed and what percentage of the total that represents.
- `total_tests = 100`
- `failed_tests = 5`
- `passed_tests = total_tests - failed_tests`
- `pass_percentage = (passed_tests / total_tests) * 100`


### Exercise 5: Comparison and Logical Operators

Using `if-else`, check if a given test case passes or fails:
- Assign values to variables expected_output and actual_output.
- If `expected_output` equals `actual_output`, print `"Test Passed"`. Otherwise, print `"Test Failed"`.
- Add conditions where a boolean variable `is_critical` checks if the test is critical. If the test fails and `is_critical` is `True`, print `"Critical Test Failed"`.


### Exercise 6: Adding Comments

Go through your scripts from Exercises 1–5 and add comments explaining:
- What each variable represents.
- Why certain operations are performed.
- Use both single-line and multi-line comments where appropriate.


### Exercise 7: Nested `if` Statements

Write a script that checks if a user is eligible for a special test case discount:
- The user must be a registered tester and must have run at least 5 tests in the last week.
- If the user meets both conditions, print "Eligible for discount".
- If the user is registered but hasn’t run 5 tests, print "Not enough tests for discount".
- If the user is not registered, print "Not eligible for discount".


### Exercise 8: `for` Loop Iteration
Create a list of test results (e.g., [True, False, True, False]). Write a `for` loop that prints `"Test Passed"` for `True` values and `"Test Failed"` for `False` values.


### Exercise 9: While Loop with Break Condition
Simulate a test runner that will continue running test cases until all tests pass. If a critical test fails, stop the runner early using a `break` statement.

### Exercise 10: BeeCrowd Challenges Related to Variables, Data Types, Operators, Comments and Functions
Complete the following challenges on BeeCrowd to reinforce your understanding:
- [1000: Hello World!](https://judge.beecrowd.com/en/problems/view/1000)
- [1001: Extremely Basic](https://judge.beecrowd.com/en/problems/view/1001)
- [1004: Simple Product](https://judge.beecrowd.com/en/problems/view/1004)
- [1035: Selection Test 1](https://judge.beecrowd.com/en/problems/view/1035)
- [1044: Multiples](https://judge.beecrowd.com/en/problems/view/1044)
- [1066: Even, Odd, Positive, and Negative](https://judge.beecrowd.com/en/problems/view/1066)
- [1014: Consumption](https://judge.beecrowd.com/en/problems/view/1014)
- [1017: Fuel Spent](https://judge.beecrowd.com/en/problems/view/1017)
- [1021: Banknotes and Coins](https://judge.beecrowd.com/en/problems/view/1021)
- [1038: Snack](https://judge.beecrowd.com/en/problems/view/1038)
- [1047: Game Time with Minutes](https://judge.beecrowd.com/en/problems/view/1047)
- [1036: Bhaskara's Formula](https://judge.beecrowd.com/en/problems/view/1036)
- [1041: Coordinates of a Point](https://judge.beecrowd.com/en/problems/view/1041)
- [1049: Animal](https://judge.beecrowd.com/en/problems/view/1049)
- [1050: DDD](https://judge.beecrowd.com/en/problems/view/1050)
- [1065: Even Between Five Numbers](https://judge.beecrowd.com/en/problems/view/1065)

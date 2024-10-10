# Week 2: Data Structures for Test Data

## Introduction

In this week, we will delve into various data structures in Python that are essential for managing test data in automation. Data structures provide a means to store, organize, and manipulate data efficiently, allowing for more effective test scripts. We will cover lists, tuples, dictionaries, and sets, exploring their features and practical applications in test automation.

## Why Data Structures Matter in Test Automation

In test automation, managing test data efficiently is critical. You might be dealing with sets of input values, expected outputs, or configurations that need to be structured in a way that makes them easy to access and modify. Data structures are the backbone of any such storage mechanism.

By using data structures, test automation becomes `scalable` and `maintainable`. You can dynamically generate or modify test data instead of hard coding it in multiple places.


## What You Will Learn:
- Basic Python data structures: lists, tuples, dictionaries, and sets.

---


### [Section 1](section01.md): Lists

### [Section 2](section02.md): Tuples

### [Section 3](section03.md): Dictionaries

### [Section 4](section04.md): Sets


## Task Exercises:

These tasks should be delivered/solved in maximum 1 week (next Friday):

1. Research about the `Bubble Sort Algorithm` in Python. Implement three version of it:
- In ascending order (regular one)
- In descending order
- With early stopping

2. Research about `Caching Mechanism` and then, implement a caching mechanism for a function that calculates the square of a number. Instructions:
- Define a function `square(n)` that calculates the square of an input number n.
- Implement a cache using a dictionary to store previously computed squares.
- Modify the `square(n)` function to check if the result for the given n is already in the cache:
  - If it is, return the cached result.
  - If it is not, compute the square, store it in the cache, and then return the result.

3. Research about `fronzenset()`. You are building a test automation framework and want to store a collection of test case scenarios (with unique steps) in an immutable set so that the test scenarios can’t be altered. Each test scenario is a list of test steps, and you want to avoid duplicates.
- Use `frozenset()` to store the test steps of each scenario in an immutable set.
- Store each test scenario in a dictionary where the key is the test case name and the value is the `frozenset` of steps
- Write a function that, given a test case name, prints whether the scenario already exists in the dictionary
- Examples of test steps for different scenarios:
  - `steps_1 = ["open browser", "navigate to page", "click login"]`
  - `steps_2 = ["open browser", "navigate to page", "fill form"]`
  - `steps_3 = ["open browser", "navigate to page", "click login"]`  # duplicate steps

4. Complete the following challenges on BeeCrowd:
- [1011: Volume of a Sphere](https://judge.beecrowd.com/en/problems/view/1011)
- [1041: Point Location](https://judge.beecrowd.com/en/problems/view/1041)
- [1071: Sum of Consecutive Integers](https://judge.beecrowd.com/en/problems/view/1071)
- [1094: Experiment](https://judge.beecrowd.com/en/problems/view/1094)
- [1020: Age in Days](https://judge.beecrowd.com/en/problems/view/1020)
- [1051: Tax Calculation](https://judge.beecrowd.com/en/problems/view/1051)
- [1093: K-Substring](https://judge.beecrowd.com/en/problems/view/1093)
- [1050: DDD](https://judge.beecrowd.com/en/problems/view/1050)
- [1065: Even Between Five Numbers](https://judge.beecrowd.com/en/problems/view/1065)

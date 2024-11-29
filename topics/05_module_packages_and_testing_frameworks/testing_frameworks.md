# Section 3: Testing Frameworks

A test automation framework is a structured set of guidelines, libraries, and tools designed to facilitate the creation, execution, and maintenance of automated test scripts. It defines how tests are organized, the rules for writing scripts, and the mechanisms for executing them across various environments. 

Writing and maintaining automated tests can be challenging and time-consuming, especially as a codebase grows in size and complexity. Framework approach in automation solves these problems by combining techniques and tools to proceed with tests more effectively.


## References:

1. [Framework approach in automation - Wikipedia](https://en.wikipedia.org/wiki/Test_automation#Framework_approach_in_automation)
2. [pytest](https://docs.pytest.org/en/stable/#)
3. [pytest - How to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html#mark)
4. [pytest - How to parametrize fixtures and test functions](https://docs.pytest.org/en/stable/how-to/parametrize.html#parametrize-basics)
5. [pytest - Teardown/Cleanup](https://docs.pytest.org/en/stable/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization)
6. [unittest - Unit testing framework](https://docs.python.org/3/library/unittest.html)


## 3.1 What Is a Test Automation Framework?

A test automation framework is a set of guidelines, rules, and best practices that are used to create and design test cases. It provides an environment for automating and executing tests, helping testers ensure consistency, maintainability, and scalability of the testing process. The framework generally includes methods to handle test data, reusable code modules, reporting mechanisms, and tools for driving tests. It helps improve test accuracy and decrease test maintenance, making automated testing more efficient and reliable.


## 3.2 Types of Test Automation Frameworks

**Linear Scripting Framework:** Also known as "Record and Playback", this framework records test steps executed by the tester and generates scripts. It doesn't require any programming knowledge but is hard to maintain and scale.

Example: Selenium IDE - This tool offers a record-and-playback feature which records user interactions with the web browser and plays them back to test whether the interactions produce the expected results. This is best suited for small projects and simple tests where maintainability is not a big concern.

**Modular Testing Framework:** Tests are divided into small, independent scripts representing modules, functions, or parts of the application. Each is tested separately, then combined to build larger tests.

TestComplete is a good example of a modular testing framework. It allows testers to create small, reusable scripts for different parts of an application, 

**Data Driven Framework:** This framework separates test scripts from test data, allowing testers to store data externally. Test data can be sourced from database or spreadsheets, enabling reusability and easier maintenance.

Apache JMeter is an example of a data-driven framework. It allows testers to separate test scripts from test data, which can be stored in external files like Excel spreadsheets, databases, or XML files

**Keyword-Driven Framework:** It involves the use of a table format to define keywords or action words for each function or method which an automation tool can understand and execute.

QTP/UFT (Unified Functional Testing) is a well-known keyword-driven framework. It uses a table format to define keywords for each function or method, which the automation tool can then execute.

**Hybrid Testing Framework:** This framework combines features of more than one of the above frameworks to leverage the strengths and mitigate the weaknesses of each.

Serenity (formerly Thucydides) is an example of a hybrid testing framework. It combines features of data-driven and keyword-driven frameworks to leverage the strengths of both.

## 3.3 Test Automation Framework Architecture

A typical test automation framework architecture includes several components such as:

- Test Management Tools: To manage test cases, scripts, and reporting.
- Function Libraries: Reusable code that can be used across multiple test cases.
- Test Data Sources: External sources like databases or files to handle data inputs.
- Test Drivers: To drive the execution of tests.
- Reporting Tools: To generate test execution reports and logs.

A **Layered Architecture** is the most commonly known architecture pattern. It is often used as a base for test automation framework architecture. According to the approach, modules or components with similar functionalities are organized into horizontal layers.

The most known and widely used architecture for test automation frameworks is a three-layered architecture: Data, Business, and Core layers.

- On the core layer, there are entities that belong to the entire framework and are not specific to the application. For example, it could be an API client, which implements main methods: GET, POST, PUT, DELETE. This layer does not have any details, such as URLs or body of a request.


### Example:

```python
def get_request(self, url, headers, params):
    pass
```

- Business layer provides methods depending on the functionality specific to the application under test.


### Example:

```python
def get_all_users(self):
    return self.get_request(url='api/users')
```

- Data layer stores all the data that is necessary to proceed with the business layer. For example, login and password for users for a particular test environment.


### Example:

```python
# configs (package)
    # environment.yaml (YAML file)
    envs:
        dev:
            user: abc
            password: 12345678
        qa: 
            user: xyz
            password: 87654321
```

**Summary** The business layer knows what it interacts with and what it does. The core layer knows how to do it. And the data layer knows what else needs to be provided for the whole system to work.


## 3.4 Pytest

Pytest is a popular testing framework that lets you write simple, scalable test cases for databases, APIs, or UIs in Python.

Here are some key features of Pytest:

- **Simple and flexible:** Tests can be written as simple functions, no need for OOP boilerplate.
- **Assert introspection:** Provides detailed information about failing assert statements without needing extra code.
- **Fixtures:** Can be used to set up and tear down code for tests, can be scoped at different levels (function, class, module).
- **Plugins:** Pytest has a vast ecosystem of plugins that extends its functionalities.
- **Parametrization:** Can run the same test functions with different data inputs, making it easier to cover edge cases.
- **Parallel test execution:** With plugins, Pytest can execute tests in parallel, reducing test run times.


### 3.4.1 Install pytest

Run the following command in your command line: `pip install -U pytest`


### 3.4.2 Create your first test


### Example:

```python
# test_one.py
def my_func(x):
    return x + 1

def test_my_func():
    assert my_func(3) == 5
```

```python
# output
============================= test session starts =============================
collecting ... collected 1 item

test_one.py::test_my_func FAILED                                         [100%]
test_one.py:19 (test_my_func)
4 != 5

Expected :5
Actual   :4
<Click to see difference>

def test_my_func():
>       assert my_func(3) == 5
E       assert 4 == 5
E        +  where 4 = my_func(3)

test_one.py:21: AssertionError


============================== 1 failed in 0.10s ==============================

Process finished with exit code 1
```


### 3.4.3 Group multiple tests in a class

Use classes to group your tests:


### Example:

```python
# test_one.py
def my_func(x):
    return x + 1


class TestClass:

    def test_my_func_one(self):
        assert my_func(3) == 5

    def test_my_func_two(self):
        assert my_func(-1) == 0
```

```python
# output
============================= test session starts =============================
collecting ... collected 2 items

test_one.py::TestClass::test_my_func_one 
test_one.py::TestClass::test_my_func_two 

========================= 1 failed, 1 passed in 0.11s =========================
FAILED                          [ 50%]
test_one.py:6 (TestClass.test_my_func_one)
4 != 5

Expected :5
Actual   :4
<Click to see difference>

self = <test_one.TestClass object at 0x000002465736B100>

    def test_my_func_one(self):
>       assert my_func(3) == 5
E       assert 4 == 5
E        +  where 4 = my_func(3)

test_one.py:8: AssertionError
PASSED                          [100%]
Process finished with exit code 1
```

Grouping tests in classes can be beneficial for the following reasons:

- Test organization
- Sharing fixtures for tests only in that particular class
- Applying marks at the class level and having them implicitly apply to all tests


### 3.4.4 Test fixtures

A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

In pytest, they are functions you define that serve this purpose. We can tell pytest that a particular function is a fixture by decorating it with `@pytest.fixture`.


### Example:

```python
# test_one.py
import pytest


def my_func(x):
    return x + 1


@pytest.fixture()
def my_fixture():
    print('DB connection established')


def test_my_func(my_fixture):
    assert my_func(3) == 5
```

```python
# output
============================= test session starts =============================
collecting ... collected 1 item

test_one.py::test_my_func DB connection established
FAILED                                         [100%]
test_one.py:12 (test_my_func)
4 != 5

Expected :5
Actual   :4
<Click to see difference>

my_fixture = None

    def test_my_func(my_fixture):
>       assert my_func(3) == 5
E       assert 4 == 5
E        +  where 4 = my_func(3)

test_one.py:14: AssertionError


============================== 1 failed in 0.11s ==============================

Process finished with exit code 1

```

A fixture is only available for tests to request if they are in the scope that fixture is defined in. If a fixture is defined inside a class, it can only be requested by tests inside that class. But if a fixture is defined inside the global scope of the module, then every test in that module, even if it’s defined inside a class, can request it.

**Note** Fixtures defined in a `conftest.py` can be used by any test in that package without needing to import them (pytest will automatically discover them). Read more about ficture scopes [here](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes).


### 3.4.5 Parametrizing test functions

The builtin `pytest.mark.parametrize` decorator enables parametrization of arguments for a test function. In the example below, the `@parametrize` decorator defines three different `(test_input, expected)` tuples so that the `test_my_func` function will run three times using them in turn:


### Example:

```python
# test_one.py
import pytest


def my_func(x):
    return x + 1


@pytest.mark.parametrize("test_input, expected", [(1, 2), (-1, 0), (3, 5)])
def test_my_func(test_input, expected):
    assert my_func(test_input) == expected
```

```python
# output
============================= test session starts =============================
collecting ... collected 3 items

test_one.py::test_my_func[1-2] 
test_one.py::test_my_func[-1-0] 
test_one.py::test_my_func[3-5] 

========================= 1 failed, 2 passed in 0.13s =========================
PASSED                                    [ 33%]PASSED                                   [ 66%]FAILED                                    [100%]
test_one.py:7 (test_my_func[3-5])
4 != 5

Expected :5
Actual   :4
<Click to see difference>

test_input = 3, expected = 5

    @pytest.mark.parametrize("test_input, expected", [(1, 2), (-1, 0), (3, 5)])
    def test_my_func(test_input, expected):
>       assert my_func(test_input) == expected
E       assert 4 == 5
E        +  where 4 = my_func(3)

test_one.py:10: AssertionError

Process finished with exit code 1
```

**Note** You could also use the parametrize marker on a class or a module.


### Practical Exercises (Drills):

1. Name benefits which a three-layered architecture brings for Test Automation Framework.
2. What is a test runner?
3. How to skip all functions in a class in pytest?
4. Given the below Python class, use Pytest to write 2 test cases to verify:
- TC01:  the functionality of the "add" method. Parametrize this TC with at least 3 different values.
- TC02: the exception handling of the "divide" method. Also, the exception message should be validated.

```python
import pytest
class Calculator:
    def add(self, a, b):
        return a + b
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


# TODO TC01: Add the parametrization decorator and then, change the function below to use it
def test_add():
    pass

# TODO TC02: Change the function below to assert about expected exceptions
def test_divide():
    pass
```

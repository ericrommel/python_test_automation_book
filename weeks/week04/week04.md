# Week 4: Introduction to Object-Oriented Programming (OOP) for Test Automation

We will cover how to apply `Object-Oriented Programming` (`OOP`) concepts in `Python` to write scalable and maintainable test scripts. `OOP` helps create structured test automation frameworks where code is modular, reusable, and easy to manage.


Why `OOP` matters in Test Automation?
- **Modularity:** Test scripts become easier to maintain when they are modularized using classes.
- **Reusability:** Common functionalities can be abstracted into base classes and reused across different test cases.
- **Scalability:** `OOP` allows test frameworks to grow by organizing test cases and methods into logical units.


The core principles of `OOP` are:
- **Encapsulation**
- **Abstraction**
- **Inheritance**
- **Polymorphism**


## References
- [Python Classes and Objects - Official Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming in Python - Real Python](https://realpython.com/python3-object-oriented-programming/)
- [Inheritance in Python - Programiz](https://www.programiz.com/python-programming/inheritance)
- [Understanding MRO (Method Resolution Order) for old and new style classes in python](https://medium.com/geekculture/understanding-mro-method-resolution-order-for-old-and-new-style-classes-in-python-f541747c48c7)

---


## 4.1 `OOP` Basics


## 4.1.1 Classes and Objects

A `class` is a blueprint (contract or plan) for creating objects, defining the attributes (properties or data) and methods (behavior) that its objects will have.

We can think of a `class` as an abstraction of real-world entities - one of the core principles of `Object-Oriented Programming` (`OOP`).

Abstraction involves simplifying complex systems by modeling classes that represent real-world entities while hiding unnecessary details. By defining a `class`, we focus only on the attributes and behaviors that are relevant to the program, leaving out irrelevant complexities. For instance, when creating a `Car` class, we only include essential attributes like `make`, `model`, and `year`, as well as key behaviors (methods) like `displaying information`, rather than every possible detail of a real car. This abstraction makes the code more understandable and maintainable.

When we create a new `class`, we're also defining a new type of object in Python, giving us a custom data type to represent specific entities in our code.


An `object` is an instance of a class, representing a concrete implementation of that blueprint. In Python, every `object` is created from a `class`. While all objects of a `class` share the same structure (attributes and methods), each instance can hold unique values for those attributes, allowing different instances to represent different data.


### Example

```python
class TestCase:
    # Constructor of the class
    def __init__(self, name):
        self.name = name  # Attribute/Property/State

    def run(self): # Method/Behaviour
        print(f"Running test case: {self.name}")

# Create an object (test case) from the class
test = TestCase("Login Test")
test.run()  # Output: Running test case: Login Test
```


```python
class Car:
    def __init__(self, make, model, year):
        self.make = make      # Car manufacturer
        self.model = model    # Car model
        self.year = year      # Manufacturing year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2020)

# Using the display_info method for each car
print(car1.display_info())  # Output: 2022 Toyota Camry
print(car2.display_info())  # Output: 2020 Honda Civic

print(type(car1))  # Output: <class '__main__.Car'>
print(type(car2))  # Output: <class '__main__.Car'>
```

**Note:** `self` is a reference to the current instance of a class. It is used to access variables and methods associated with the instance. When you create an object of a class, `self` allows you to work with that specific object's attributes and methods. It must always be the first parameter of instance methods, but it is not required to be named self, it is a convention.


## 4.1.2 The `__init__` method (Constructor)

The `__init__` method, also known as the `constructor`, is used to initialize an object's attributes when the object is created. However, this method is optional. If a class doesn't define an `__init__` method, `Python` will provide a default constructor, which doesn't initialize any attributes.

In `Python`, it is not possible to have multiple `__init__` methods in the same class, like in other languages such as `Java`, which support **method overloading** (having multiple methods with the same name but different parameter signatures).

Defining multiple `__init__` methods or any kind of methods with the same name will cause the last one defined to override any previous ones. However, you can achieve similar behavior by using default arguments or checking the arguments passed to the methods.


### Example

```python
class TestCase:
    def __init__(self, name=None, description=None):
        if name and description:
            self.name = name
            self.description = description
            print(f"TestCase with name: {self.name} and description: {self.description}")
        elif name:
            self.name = name
            print(f"TestCase with name: {self.name}")
        else:
            print("TestCase with no name or description")

# Create instances with different arguments
test1 = TestCase("Login Test", "Tests the login functionality")
test2 = TestCase("Signup Test")
test3 = TestCase()
```


## 4.1.3 The `@dataclass` Decorator

The `@dataclass` decorator, available in the `dataclasses` module, simplifies the creation of classes by automatically generating common methods such as `__init__`, `__repr__`, and `__eq__`. This is especially useful when your class is mainly used to store data, which is often the case in test automation scripts.

- `__init__`: method to initialize attributes.
- `__repr__`: method for easy debugging and logging.
- `__eq__`: which can be useful for asserting equality in tests.


**Curiosity:** In Python, methods that are between double underscores, like the above ones, are called **Magic Methods** or **Dunder Methods**. Learn more about it [here](https://realpython.com/courses/magic-methods-classes/).


## Example without `@dataclass`

```python
class TestResult:
    def __init__(self, test_name, status, duration):
        self.test_name = test_name
        self.status = status
        self.duration = duration

    def __repr__(self):
        return f"TestResult(test_name={self.test_name}, status={self.status}, duration={self.duration})"

    def __eq__(self, other):
        if isinstance(other, TestResult):
            return (self.test_name == other.test_name and
                    self.status == other.status and
                    self.duration == other.duration)
        return False

result1 = TestResult("TestLogin", "Passed", 5.23)
result2 = TestResult("TestLogin", "Passed", 5.23)

print(result1)  # Output: TestResult(test_name=TestLogin, status=Passed, duration=5.23)
print(result1 == result2)  # Output: True
```

This class requires you to manually write the `__init__`, `__repr__`, and `__eq__` methods, which can be tedious for simple data classes.


## Example with `@dataclass`

```python
from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class TestResult:
    test_name: str
    status: str
    duration: float

result1 = TestResult("TestLogin", "Passed", 5.23)
result2 = TestResult("TestLogin", "Passed", 5.23)

print(result1)  # Output: TestResult(test_name='TestLogin', status='Passed', duration=5.23)
print(result1 == result2)  # Output: True
```

With `@dataclass`, Python automatically generates the `__init__`, `__repr__`, and `__eq__` methods, drastically reducing boilerplate code.

Note that you can customize the behavior of the generated methods by using parameters:

- `@dataclass(frozen=True)`: This makes instances of the class immutable.
- `@dataclass(order=True)`: This adds comparison methods (`<`, `<=`, `>`, `>=`) based on the order of attributes.


## 4.1.4 Inheritance and Method Overriding

Inheritance allows a class (child) to inherit attributes and methods from another class (parent). This is useful in test automation for creating base test classes that share common functionalities.


### Example

```python
class BaseTest:
    def setup(self):
        print("Setting up the test")

class LoginTest(BaseTest): # LoginTest inherits from BaseTest
    def run(self):
        print("Running login test")

# The child class inherits methods from the parent class
test = LoginTest()
test.setup() # Output: Setting up the test
test.run() # Output: Running login test
```

Method overriding occurs when a child class provides its own implementation of a method that exists in the parent class. In test automation, you can override methods like `setup()` or `run()` to customize the behavior of test cases.


### Example

```python
class X:
    def call(self):
        print("Calling from X")

class Y(X):
    def call(self):
        print("Calling from Y")

obj = Y()
obj.call() # Output: 'Calling from Y'
```


## 4.2 Advanced `OOP` Concepts


## 4.2.1 Multiple Inheritance

`Python` supports `multiple inheritance`. It occurs when a class inherits from more than one parent class. While useful in certain cases, it should be used cautiously as it can make the code complex.


### Example

```python
class Father:
    def hobby(self):
        return "fishing"

class Mother:
    def hobby(self):
        return "gardening"

class Child(Father, Mother):
    pass

child = Child()
print(child.hobby())  # Output: fishing
```


## 4.2.2 Method Resolution Order (MRO)

In `Python`, when a method is called on an object, the interpreter looks for the method in a specific order. This order is determined by the **Method Resolution Order** (`MRO`), which defines the hierarchy in which `Python` searches for methods in the parent classes.


### Example

```python
class BaseTest:
    def setup(self):
        print("Setting up the test")

    def teardown(self):
        print("Cleaning up the test")

class SetupMixin:
    def setup(self):
        print("Setting up common tasks")

class LoginTest(SetupMixin, BaseTest):
    def run(self):
        print("Running login test")

test = LoginTest()
test.setup() # Output: Setting up common tasks
test.run() # Output: Running login test
test.teardown() # Output: Cleaning up the test
```


**Note:** What is a `Mixin`? A `mixin` is a type of class that provides methods to other classes but is not considered a base class on its own. `Mixins` are typically used **"to include"** functionality to classes through inheritance, allowing for code reuse without creating a rigid class hierarchy. They are designed to be combined with other classes to enhance their capabilities. This approach promotes a modular design where functionalities can be shared across multiple classes. For more information about `mixins`, you can refer to [Mixin on Wikipedia](https://en.wikipedia.org/wiki/Mixin).


You can use the `mro()` method to check the method resolution order.

### Example

```python
print(LoginTest.mro())
# Output: [<class '__main__.LoginTest'>, <class '__main__.SetupMixin'>, <class '__main__.BaseTest'>, <class 'object'>]
```


## 4.2.3. The `super()` method

The `super()` method is used to refer to the parent class or superclass. It allows you to call methods defined in the superclass from the subclass, enabling you to extend and customize the functionality inherited from the parent class.

```python
class Animal:
    def do_something(self):
        print("Animal behavior")

class Canine(Animal):
    def do_something(self):
        print("Canine behavior")
        super().do_something()  # Calls Animal's method

class Pet(Animal):
    def do_something(self):
        print("Pet behavior")
        super().do_something()  # Calls Animal's method

class Dog(Canine, Pet):
    def do_something(self):
        print("Dog behavior")
        super().do_something()  # Calls the next class in the MRO (Canine)

# Create an instance of Dog
dog = Dog()
dog.do_something()

# Output:
# Dog behavior
# Canine behavior
# Pet behavior
# Animal behavior
```


Using `super()` is especially helpful in the `__init__` method to ensure that the parent class's attributes are initialized properly, even when adding new attributes in the subclass.

```python
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def make_sound(self):
        return "Some generic sound"

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, species, age, breed):
        # Initialize parent class attributes using super()
        super().__init__(species, age)
        self.breed = breed  # New attribute specific to Dog

    def make_sound(self):
        return "Bark!"

# Creating an instance of Dog
dog = Dog("Canine", 5, "Labrador")
print(dog.species)       # Output: Canine
print(dog.age)           # Output: 5
print(dog.breed)         # Output: Labrador
print(dog.make_sound())  # Output: Bark!
```


Sometimes, you may want to directly call methods from specific parent classes. Here’s how to do this with the Dog class by bypassing super() and calling each parent class’s method directly:

```python
class D(B, C):
    def do_something(self):
        print("Method from class D")
        B.do_something(self)  # Calls B's method directly
        C.do_something(self)  # Calls C's method directly
```


## 4.2.4 Encapsulation

Encapsulation means keeping data (attributes) and the methods that work on that data together in one place (a class). It helps control how the data is accessed and changed, protecting the internal details from outside interference.

In `Python`, while there are no strict access modifiers (`public`, `protected`, or `private`) found in languages like `Java` or `C++`, we use naming conventions to indicate the intended visibility of class attributes and methods.


### Access Modifiers in `Python`

- **Public Members:**
  - Attributes and methods that are defined **without any leading underscore** are public by default.
  - They can be accessed from outside the class without any restrictions.
- **Protected Members:**
  - Attributes and methods that start with a **single underscore** (`_`) are considered protected.
  - This indicates that they are intended for internal use within the class and its subclasses. While they can still be accessed from outside, it is discouraged.
- **Private Members:**
  - Attributes and methods that start with **double underscores** (`__`) are considered private.
  - They cannot be accessed directly from outside the class, as they are `name-mangled` to avoid naming conflicts in subclasses.

**Note:** `Name mangling` is a process where the interpreter changes the name of a private variable to make it harder to create accidental collisions in subclasses and less accessible from outside the class.


### Example

```python
class TestCase:
    def __init__(self, test_name):
        self.test_name = test_name    # Public attribute
        self._test_data = []          # Protected attribute
        self.__expected_result = None # Private attribute

    def add_test_data(self, data):
        """Public method to add test data."""
        self._test_data.append(data)  # Accessing protected attribute
        print(f"Data added: {data}")

    def set_expected_result(self, result):
        """Public method to set the expected result."""
        self.__expected_result = result  # Accessing private attribute
        print(f"Expected result set: {result}")

    def validate(self):
        """Public method to validate the test case."""

        # Simulating validation logic
        if self.__expected_result is not None:
            print(f"Validating {self.test_name}: {self.__expected_result}")
        else:
            print("Expected result not set for validation.")

    def __private_method(self):
        """Private method to demonstrate internal logic."""
        return "This is a private method, not accessible outside."

    def access_private_method(self):
        """Public method to access the private method."""
        return self.__private_method()


class AdvancedTestCase(TestCase):
    def display_test_data(self):
        """Public method to display protected test data."""
        print("Protected Test Data:", self._test_data)  # Accessing protected attribute


# Creating an instance of TestCase
test_case = TestCase("Sample Test")
test_case.add_test_data("Input Data 1")
test_case.set_expected_result("Expected Output")
test_case.validate()

# Accessing public attributes
print("Test Name:", test_case.test_name)

# Creating an instance of AdvancedTestCase
advanced_test_case = AdvancedTestCase("Advanced Test")
advanced_test_case.add_test_data("Advanced Input Data")
advanced_test_case.display_test_data()

# Attempting to access private attribute (will raise an error)
# print(test_case.__expected_result)  # Raises an AttributeError

# Accessing a private attribute using "name mangling"
print("Accessing private attribute:", test_case._TestCase__expected_result)  # Works due to name mangling but it is not recommended in practice

# Accessing private method through a public method
print(advanced_test_case.access_private_method())  # Output: This is a private method, not accessible outside.
```


## 4.2.5 Polymorphism

Polymorphism in `Python` allows objects of different classes to be treated as objects of a common super class. The most common use of polymorphism is when a parent class reference is used to refer to a child class object. This feature is essential in Test Automation, as it enables the creation of flexible and easily extensible test frameworks. In simpler terms, polymorphism lets you define methods in different classes that have the same name but behave differently.


### Example

```python
class TestCase:
    def run_test(self):
        raise NotImplementedError("Subclasses must implement this method.")

class UnitTest(TestCase):
    def run_test(self):
        print("Running unit test...")

class IntegrationTest(TestCase):
    def run_test(self):
        print("Running integration test...")

class PerformanceTest(TestCase):
    def run_test(self):
        print("Running performance test...")

# Using polymorphism
def execute_tests(tests):
    for test in tests:
        test.run_test()  # Calls the appropriate run_test() method

# Test instances
unit_test = UnitTest()
integration_test = IntegrationTest()
performance_test = PerformanceTest()

# List of test cases
test_cases = [unit_test, integration_test, performance_test]

# Execute all tests
execute_tests(test_cases)
```


## 4.2.6 Static Methods

Static methods are defined using the `@staticmethod` decorator. They don't require an instance of the class to be called and don't have access to `self` or `cls`. Static methods can be used when some processing related to the class needs to be done but does not require access to any class or instance variables.


### Example

```python
class MathUtils:
    @staticmethod
    def add(a, b): # Note that there is no `self` here
        return a + b

# Calling static method without creating an instance
result = MathUtils.add(5, 3)
print(f"The sum is: {result}")  # Output: The sum is: 8
```


## 4.2.7 Class Methods

Class methods are methods that are called on the class itself, not on a specific object instance. Therefore, it belongs to a class level, and all class instances share a class method. To define a class method, you should use the `@classmethod` decorator and it takes `cls` (the class itself) as its first parameter. Use @classmethod when you need to access or modify class-level data (class variables) or when you want to define a factory method that returns an instance of the class.


### Example

```python
class TestSuite:
    test_count = 0  # Class variable to count tests

    def __init__(self, name):
        self.name = name

    @classmethod
    def increment_count(cls):
        cls.test_count += 1  # Accessing class variable
        print(f"Total tests: {cls.test_count}")

# Using the class method
TestSuite.increment_count()  # Output: Total tests: 1
TestSuite.increment_count()  # Output: Total tests: 2
```


### Key Differences between `@classmethod` and `@staticmethod`

| Feature             | `@classmethod`                              | `@staticmethod`                                      |
|---------------------|---------------------------------------------|------------------------------------------------------|
| First Parameter     | Takes `cls` (the class itself)              | Does **NOT** take `self` or `cls`                    |
| Access to Variables | Can access and modify class variables       | Cannot access or modify instance or class variables  |
| Use Case            | When you need to work with class-level data | When you don’t need access to class or instance data |


## 4.2.8 Abstract Classes

Abstract Classes provide a contract for other classes. They can have both concrete methods (with implementation) and abstract methods (without implementation). It can be represented using abstract base classes (`ABCs`) from the `abc` module. They specify a set of methods that must be created within any child class built from the abstract base class. Abstract classes cannot be instantiated directly.

The `@abstractmethod` decorator is used within abstract classes to define methods that must be implemented by any subclass. An abstract method has no implementation in the base class.

The `@abstractclassmethod` is a combination of `@classmethod` and `@abstractmethod`. It ensures that subclasses must implement a class method.

The `@abstractstaticmethod` combines `@staticmethod` and `@abstractmethod`, requiring subclasses to implement a static method.

These decorators ensure that subclasses implement specific methods. You can learn more about them in Python's [Official Documentation](https://docs.python.org/3/library/abc.html) on abstract base classes.


### Example

```python
from abc import ABC, abstractmethod

class TestCase(ABC):  # Abstract class
    @abstractmethod
    def run_test(self):
        pass

class UnitTest(TestCase):
    def run_test(self):
        print("Running unit test...")

class IntegrationTest(TestCase):
    def run_test(self):
        print("Running integration test...")

# Attempting to instantiate TestCase will raise an error
# test_case = TestCase()  # This would raise: TypeError: Can't instantiate abstract class TestCase without an implementation for abstract method 'run_test'

# Using the classes
def execute_tests(tests):
    for test in tests:
        test.run_test()

unit_test = UnitTest()
integration_test = IntegrationTest()

test_cases = [unit_test, integration_test]
execute_tests(test_cases)
```


## Practical Exercises (Drill)

- [TI] What are the four main principles (pillars) of Object-Oriented Programming (name and explain)?
- Write a TestCase class with methods for `setup()`, `run()`, and `teardown()`. Create objects of the TestCase class to represent individual test cases.
- Investigate what the `Diamond Problem` is in the context of multiple inheritance in OOP. How can you mitigate this problem in your designs?
- Implement method overriding in a test automation context. Override a method in the child test class to customize the test execution.
- Create a multiple inheritance example: Write a class that inherits from multiple parent classes (e.g., BaseTest and a custom mixin class), and check how MRO impacts method calls.
- [TI] What are `@classmethod` and `@staticmethod` and their main differences?
- [TI] What will be the MRO for class `W` (`W.mro()`)? What is the output after the `w.call()` execution?
    ```python
    class X:
        def call(self):
            print("Calling from X")

    class Y(X):
        def call(self):
            print("Calling from Y")

    class Z(X):
        def call(self):
            print("Calling from Z")

    class W(Y, Z):
        def call(self):
            super().call()

    w = W()
    w.call()
    ```

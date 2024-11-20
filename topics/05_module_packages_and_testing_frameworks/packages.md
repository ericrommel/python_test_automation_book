# Section 2: Packages

A package in Python is a directory that contains a collection of modules (which are covered in a previous [section](modules.md)).

During test automation framework development, you will create many modules and it will be difficult to maintain them if they are all placed in one location.

### Example:

```python
# test_automation_framework (a root directory for TAF modules)
  # api.py (module implements the Requests API)
  # test_ui.py (module implements some UI test)
  # test_data_create_user.py (module implements some test data for a test)
  # base_test.py (module implements base test class)
```

Packages are a way of structuring Python’s module namespace by using “dotted module names”. Packages help avoid collisions between module names.


## References:

1. [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/#python-packages)
2. [Packages - Python Documentation](https://docs.python.org/3/tutorial/modules.html#packages)
3. [Package and Module Names - PEP-8](https://peps.python.org/pep-0008/#package-and-module-names)


## 2.1 Creating Package

Creating a package is quite straightforward, since it makes use of the operating system’s inherent hierarchical file structure.

### Example:

```python
# test_automation_framework (a root directory for TAF modules)
  # src (a package for source code)
    # base_test.py (module implements base test class)
  # tests (a package for tests)
    # test_ui.py (module implements some UI test)
```

Here, there is a directory named `test_automation_framework` that contains two packages, `src` and `tests`. Each package contains a module. Users of the package can import individual modules from the package with dot notation:

### Example:

```python
# test_ui.py
import src.base_test
```

An alternative way of importing the module is:

```python
# test_ui.py
from src import base_test
```

**[Note]** You can technically import the package as well

### Example:

```python
# test_ui.py
import src
```

but it does not place `base_test` module into the local namespace.


## 2.2 Initializing Package

If a file named `__init__.py` is present in a package directory, it is invoked when the package or a module in the package is imported. This file helps the Python interpreter understand that this directory is a package. `__init__.py` can just be an empty file, but it can also execute initialization code for the package.

### Example:


```python
# src.__init__.py
print(f'Invoking __init__.py for {__name__}')
```

```python
# tests.__init__.py
# empty file
```

```python
# test_automation_framework
  # src
    # __init__.py
    # base_test.py
  # tests
    # __init__.py
    # test_ui.py
```

Now when the package is imported, you will see the following output:

```python
# test_ui.py
import src.base_test

#output: Invoking __init__.py for src
```


## 2.3 Automatic Importing

`__init__.py` can also be used to effect automatic importing of modules from a package. If `__init__.py` in the pkg directory contains the following: `import pkg.mod1, pkg.mod2`, then when you execute `import pkg`, modules `mod1` and `mod2` are imported automatically.


### Example:

```python
# src.__init__.py
print(f'Invoking __init__.py for {__name__}')
import src.base_test
```

```python
# test_automation_framework
  # src
    # __init__.py
    # base_test.py
  # tests
    # __init__.py
    # test_ui.py
```

```python
# test_ui.py
import src

#output: Invoking __init__.py for src
```


## 2.4 Subpackages

Packages can contain nested **subpackages** to arbitrary depth. Importing still works the same as shown previously, but additional dot notation is used to separate package name from subpackage name.


### Practical Exercises (Drills):
1. Modify the example package directory by adding a subpackage. How import syntax should be modified?
2. Why much of the Python documentation states that an `__init__.py` file must be present in the package directory when creating a package?
3. What happens when user tries importing * From a Package?
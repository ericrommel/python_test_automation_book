# Section 1: Modules

Python modules and Python packages (which will be covered in the next [section](packages.md)), are two mechanisms that facilitate modular programming.

Modular programming refers to the process of breaking a large programming task into separate, smaller, more manageable subtasks or modules. In test automation, we use individual modules as building blocks to create a test automation framework.

### Example:

```python
# requests (a package for Python HTTP library)
  # api.py (requests.api module implements the Requests API)
  # auth.py (requests.auth module contains the authentication handlers for Requests)
  # session.py (requests.session module provides a Session object to manage and persist settings across requests (cookies, auth, proxies))
```

There are several advantages of storing code in modules:

- Reusability of code: Functionality defined in a single module can be easily reused across different test.
- Maintainability: If a module is independent, it makes it easier to maintain and update as a test automation framework evolves.
- Readability and Manageability: A module typically focuses on one relatively small portion of the problem, which makes development and debugging easier.
- Scoping: Modules define a separate namespace, which helps avoid collisions between names in different areas of a test automation framework.

**Note**: You can think of a namespace as a place where a variable is stored. Namespaces support modularity by preventing naming conflicts. They also aid readability and maintainability by making it clear which module implements a function. For instance, the functions `builtins.open` and `os.open()` are distinguished by their namespaces.


## References:

1. [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/#python-modules-overview)
2. [Modules - Python Documentation](https://docs.python.org/3/tutorial/modules.html#)
3. [The import system - Python Documentation](https://docs.python.org/3/reference/import.html)
4. [Namespaces and Scope in Python](https://realpython.com/python-namespaces-scope/)
5. [Imports - PEP-8](https://peps.python.org/pep-0008/#imports)


## 1.1 Defining Module

A module is a file with the suffix `.py` containing Python definitions and statements. It is essential to know that there are different ways to define a module in Python:

1. A module can be written in Python itself.
2. A module can be written in C and loaded dynamically at run-time. A module can be written also in Java languages, when using Jython (it depends on the Interpreter, as to which one you use).
3. A built-in module is intrinsically contained in the interpreter.

The module’s name (as a string) is available as the value of the global variable `__name__`.


## 1.2 Accessing Module's Content

A module content is accessed with the `import` statement.

### Example:

```python
import re # importing the whole module re
```

When an `import` statement is executed, Python searches for the named module by calling the `__import__()` function. If the module is found, it creates a module object and initializing it. Then it binds the results of that search to a name in the local scope. If the named module cannot be found, a `ModuleNotFoundError` is raised.

Using the module name you can access the functions:

### Example:

```python
import time
time.sleep(30)  # Access sleep() from the standard module. Only the module name is added to the current namespace.
```

Instead of importing the whole module, you can import only some names:

### Syntax:

```python
from [module name] import [name]
```

### Example:

```python
from time import sleep
sleep(30)  # sleep name is imported from a module directly into the importing module’s namespace. 
```

It is also possible to import an object but add it with an alternate name:

### Syntax:

```python
from [module name] import [name] as [your module alias]
```

### Example:

```python
from time import sleep as my_local_sleep
my_local_sleep(1) 
```

There is a variant to import all names that a module defines:

### Syntax:

```python
from [module name] import *
```

This imports all names except those beginning with an underscore `_`. Try to avoid using this facility since it introduces an unknown set of names and might overwrite an existing name as Python will call the method from the last import.


## 1.3 Searching Modules

When the interpreter executes the `import` statement,  it searches for the name of the module in the following sources:

- The directory from which the input script was run or the current directory if the interpreter is being run interactively
- The list of directories contained in the `PYTHONPATH` environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

### Example:

```python
import sys
print(sys.path) # Output will be the resulting search path 
```

Once a module has been imported, you can determine the location where it was found with the module’s `__file__` attribute:

### Example:

```python
import re
re.__file__ # Output: re.py file location 
```


## 1.4 Executing Module

Any `.py` file that contains a module is essentially also a Python script and can be executed like one. Python runs all the code before importing it.

When a .py file is imported as a module, Python sets the special dunder variable `__name__` to the name of the module. However, if a file is run as a standalone script, `__name__` is set to the string `'__main__'`. This can be used to distinguish between when the file is loaded as a module and when it is run as a standalone script.

### Example:

```python
if (__name__ == '__main__'):
    print('Executing as standalone script')
```


## 1.5 Cyclic Imports

Suppose you have the following two files: `module_a.py` and `module_b.py`. Each file tries to import functions from one another.

### Example:

```python
# module_a.py
from import_b import boo
def foo():
    pass
```
```python
# module_b.py
from import_a import foo
def boo():
    pass
```

Run the `module_b.py`. You will get the following error:

```python
ImportError: cannot import name 'foo' from partially initialized module 'import_a' (most likely due to a circular import)
```

In this example, the `import` statements create a cyclic loop. To solve this problem you can refactor the code and create a new module with common functionality. Both modules can then import this common module.

### Example:

```python
# common.py
def shared_function():
    pass
```
```python
# module_a.py
from common import shared_function

def foo():
    pass
```
```python
# module_b.py
from common import shared_function

def boo():
    pass
```

Another possible solution is to put imports inside functions so that imports will occur whenever functions are called.

### Example:

```python
# module_a.py
def foo():
    from module_b import boo
    pass
```
```python
# module_b.py
def boo():
    from module_a import foo
    pass
```

Lastly, a try statement with an except `ImportError` clause can be used to guard against unsuccessful import attempts:

### Example:

```python
# module_a.py
try:
    from import_b import boo
except ImportError:
    print('Cannot import name "boo"')
def foo():
    pass

# Output: Cannot import name "boo"
```
```python
# module_b.py
from import_a import foo
def boo():
    pass
```

### Practical Exercises (Drills):
1. Create a module. Print some text and define a function.
2. What built-in function is used to print the list of defined names in a namespace?
3. Create one more module. Import the function from the first exercise. Run the module and explain the result.
4. [TI] Explain why it is bad practice to use the `from module import *` style of importing?
5. What is module's name naming convention? How import should be grouped in a module?
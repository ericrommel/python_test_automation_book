# Section 1: Modules

Python modules and Python packages (which will be covered in the next section), two mechanisms that facilitate modular programming.

According to modular programming concept, large tasks are broken into smaller manageable subtasks or modules. Modularized code has the following benefits:

- Readability
- Maintainability
- Reusability
- Scoping
- Manageability

In this section will show how to create and import a module in Python.

## References:

1. [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/#python-modules-overview)
2. [Modules - Python Documentation](https://docs.python.org/3/tutorial/modules.html#)
3. [The import system - Python Documentation](https://docs.python.org/3/reference/import.html)
4. [Imports - PEP-8](https://peps.python.org/pep-0008/#imports)

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
from import_b import boo
def foo():
    pass
```
```python
from import_a import foo
def boo():
    pass
```

Run the `module_b.py`. You will get the following error:

```python
ImportError: cannot import name 'foo' from partially initialized module 'import_a' (most likely due to a circular import)
```

In this example, the `import` statements create a cyclic loop.

### Practical Exercises (Drills):
1. Create a module. Print some text and define a function.
2. What built-in function is used to print the list of defined names in a namespace?
3. Create one more module. Import the function from the first exercise. Run the module and explain the result.
4. [TI] Explain why it is bad practice to use the `from module import *` style of importing?
5. What is module's name naming convention? How import should be grouped in a module?
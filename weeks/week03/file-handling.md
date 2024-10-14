# Section 1: File Handling in Testing

In this section, you will learn how to handle files in Python for reading and writing test data. Python provides built-in functions for file operations, such as reading, writing, and appending to files. File handling is important in test automation for managing test data that might be stored in various formats like `.txt`, `.csv`, or `.json`.


## References

1. [Official Python documentation on File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
2. [Working With Files in Python - Real Python](https://realpython.com/working-with-files-in-python/)
3. [Python File Methods - W3Schools](https://www.w3schools.com/python/python_ref_file.asp)
4. [Python File I/O - GeeksforGeeks](https://www.geeksforgeeks.org/file-handling-python/)
5. [Python Directory Management - GeeksforGeeks](https://www.geeksforgeeks.org/python-directory-management/)

---


## 1.1 Basics of File Handling

- **Opening Files**: The `open()` function is used to open files in Python.
- **Modes**: Key file modes are:
  - `"r"`: Opens the file for **reading** (default mode). The file pointer is placed at the beginning of the file. If the file does not exist, it raises a `FileNotFoundError`.
  - `"r+"`: Opens the file for both **reading and writing**. It **WON'T** erase/clean/truncate the file.
  - `"w"`: Opens the file for **writing**. If the file exists, its content will be erased. If the file does not exist, a new file is created.
  - `"w+"`: Opens the file for both writing and reading. It **WILL** erase/clean/truncate the file.
  - `"a"`: Opens the file for **appending**. The file pointer is placed at the end of the file if it exists. If the file does not exist, a new file is created.
  - `"a+"`: Opens the file for both appending and reading. You can append new data to the file and read its content, but you cannot modify the existing content.
  - `"b"`: Opens the file in **binary mode**. Used with other modes like `rb` (read binary), `wb` (write binary), etc.
  - `"t"`: Opens the file in **text mode** (default). Used with other modes like `rt` (read text), `wt` (write text), etc.

**Note:** Using the correct mode prevents accidental data loss (e.g., overwriting important files) or handles file existence checks properly.


### Syntax:

```python
# Opening a file
file = open("test_data.txt", "r")

# Reading the file
content = file.read()

# Closing the file
file.close()
```


## 1.2 Reading Files

You can read the entire file, line by line, or only specific parts of the file.

**Note:** Always use the `with` statement (context manager) to manage files. It ensures that files are properly closed after their operations, even if an exception is raised.


### Example:

```python
'''
The `read()` method reads the **entire file** content as a single string. You
can optionally pass a number to specify how many characters to read. It's often
used when you need to load everything at once, such as when dealing with smaller
files.
'''
with open("test_data.txt", "r") as file:
    content = file.read()
    print(content)


with open("test_data.txt", "r") as f:
    partial_content = f.read(100)  # Reads the first 100 characters
    print(partial_content)


'''
Read line by line. When dealing with large files, it's more efficient to read
files line by line instead of loading the entire file into memory.
'''
with open("test_data.txt", "r") as file:
    for line in file:
        print(line)
```


### Using `readline()`

The `readline()` method reads one line at a time from the file. This is useful when you want to process the file line by line, especially when the file is too large to fit in memory all at once.

```python
with open("test_data.txt", "r") as f:
    first_line = f.readline()  # Reads the first line
    print(first_line)
    second_line = f.readline()  # Reads the second line
    print(second_line)
```


### Using `readlines()`

The `readlines()` method reads all lines in the file and returns them as a `list of strings`, where each element is a line. This method is useful when you want to read the entire file but still want to handle it line by line. Each line in the list will include the newline character (`\n`).

```python
with open("test_data.txt", "r") as f:
    lines = f.readlines()  # Reads all lines into a list
    for l in lines:
        print(l)
```


## 1.3 Writing and Appending to Files

You can `write` or `append` data to a file using `write()` or `append()` methods.

````python
# Writing to a file (overwrites if exists)
with open("my_test_data.txt", "w") as file:
    file.write("This is a test.\n")

# Appending to a file
with open("my_test_data.txt", "a") as file:
    file.write("Appending this line.")
````


## 1.4 File Handling Exceptions

Handling exceptions is crucial for error-prone operations like file handling.

When using the context manager `with` in file handling, the context manager itself handles the automatic opening and closing of the file, even if an exception occurs during the operation. However, it does not handle exceptions related to file operations (like missing files or permission errors). Therefore, using a `try-except` block is necessary if you want to catch and handle exceptions such as `FileNotFoundError`, `PermissionError`, or other file-related errors.


### Example:

```python
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
```

### Handling File Exceptions Gracefully

Use specific exceptions like `FileNotFoundError`, `PermissionError`, and others to handle file-related issues.

```python
try:
    with open('data.txt', "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You don't have permission to open this file.")
```

Exceptions file-related issues:

1. `FileNotFoundError`: Raised when trying to open a file that does not exist.
2. `PermissionError`: Raised when the file cannot be accessed due to permission restrictions (e.g., trying to write to a read-only file or accessing a file you don't have rights to).
3. `IsADirectoryError`: Raised when a file operation (like `open()`) is attempted on a directory instead of a file.
4. `NotADirectoryError`: Raised when a directory operation is attempted on something that is not a directory.
5. `EOFError`: Raised when `input()` reaches the end of a file unexpectedly. This is not typically used with `open()`, but it's related to file input scenarios.
6. `OSError`: A general-purpose exception that is raised for various operating system-related errors, including file handling. `OSError` can catch various lower-level errors related to the system's handling of files.
7. `UnsupportedOperation`: Raised when an unsupported operation is attempted on a file object, such as writing to a file opened in read mode.

For more detailed information on file-related exceptions in Python, you can visit the [official Python documentation](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)


## 1.5 Using `os` and `pathlib` for Cross-Platform File Paths

To ensure your file paths work across different operating systems (Windows, Linux etc.), use `os.path` or `pathlib` modules to construct paths.

```python
from pathlib import Path

# Using pathlib for cross-platform compatibility
file_path = Path("data") / "test_file.txt"
with file_path.open("r") as file:
    content = file.read()
    print(content)
```


## 1.6 Using `seek()` and `tell()`

The `seek()` method allows you to move the file pointer to a specific position, and `tell()` tells you the current position of the file pointer.


```python
with open("data.txt", "r") as file:
    print(file.tell())  # Shows current position (e.g., 0)
    file.read(10)       # Reads the first 10 characters
    file.seek(0)        # Moves back to the beginning of the file
```


## 1.7 Handling Binary Files

When working with non-text files (e.g., images, PDFs), open them in binary mode (`"rb"`, `"wb"`)

```python
# Read a binary file (e.g., an image)
with open("image.png", "rb") as file:
    content = file.read()
    print(content)
```


## 1.8 Using `json` and `csv` for Structured Data

For test automation, structured data files like `JSON` or `CSV` are commonly used. Use the `json` and `csv` modules for easy reading and writing.

- For `json` files:

```python
import json

# Reading JSON data
with open('data.json', "r") as file:
    data = json.load(file)
```

- For `csv` files:

```python
import csv

# Reading CSV data
with open('data.csv', "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## 1.9 Using Temporary Files

For testing purposes, sometimes it’s useful to create temporary files. The `tempfile` module provides this functionality.

```python
import tempfile

# Create a temporary file
with tempfile.TemporaryFile(mode="w+") as temp_file:
    temp_file.write("Temporary test data.")
    temp_file.seek(0)
    print(temp_file.read())  # Read back the temporary data
```


## 1.10 Reading and Writing Text Files in Different Encodings

When working with files in different languages or character sets, specify the encoding explicitly to avoid encoding-related issues.

```python
# Read a file with UTF-8 encoding
with open('data.txt', "r", encoding="utf-8") as file:
    content = file.read()
```


### Practical Exercises (Drills):

1. [TI] Explain the difference between `read()`, `readline()`, and `readlines()`. In what situations would you use each?
2. [TI] How does the `with` statement help in file handling, and why is it preferred over manually opening and closing files?
3. Write a script that reads a file `test_data.txt` and prints each line.
4. Modify the script from the previous exercise to append a new line to the file.
5. Write a script that reads `test_data.txt` and counts the number of lines and words in the file. Print both counts at the end.
6. Write a script that replaces a specific word (e.g., "error") in a file `logs.txt` with the word "fixed" and saves the changes.
7. Write a script that tries to read a file `data.txt`, handles the exception if the file does not exist, and prompts the user to create the file if it's missing.
8. Merging multiple files: Write a script that reads multiple files (`file1.txt`, `file2.txt`, `file3.txt`), merges their content, and writes the result to a new file called `merged.txt`.
9. Create a script that reads a configuration file (e.g., `config.ini`) and prints out the key-value pairs. Use the `configparser` library to handle the file.
10. Write a script that reads a log file (e.g., `server.log`) and counts how many times a specific error message appears. Print the number of occurrences of that error.

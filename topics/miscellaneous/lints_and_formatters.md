# Lints and Formatters

**Lints** and **Formatters** are tools that help maintain high code quality by ensuring your code adheres to best practices, style guides, and standards.


- **Lints** analyze your code for potential errors, bad practices, or style inconsistencies. Popular linting tools include `pylint` and `flake8`. For example, a **lint** tool might warn you about an unused variable:
    ```python
    x = 10  # Unused variable (lint warning)
    print("Hello")
    ```

- **Formatters** automatically adjust your code to follow a specific style guide, such as [PEP 8](https://peps.python.org/pep-0008/). Examples include `black` and `yapf`. For instance, if your code looks like this:
    ```python
    def greet():print("  Hello  ")
    ```

    Running a formatter like `black` would reformat it to:
    ```python
    def greet():
        print("Hello")
    ```


## Ignoring Specific Rules

You can ignore specific linting or formatting rules when necessary, for individual lines, blocks, or even entire files.


### Ignoring Rules in Linting

- **Single line:** Add a `# noqa` if using `flake8` or `pylint: disable=<rule-name>` using `pylint`.

    ```python
    x = 10 # noqa: F841
    y = 10 # pylint: disable=unused-variable
    ```

- **Block of code:** `flake8` does not have a particular way to ignore block of codes. You can use `pylint` to achieve it:

    ```python
    # pylint: disable=unused-variable
    x = 10
    y = 20
    # pylint: enable=unused-variable

    z = 30 # Unused variable (lint warning)

    print("Hello")
    ```

- **Whole file:** For both `flake8` and `pylint`, add a directive at the top of the file

    ```python
    # flake8: noqa F841
    # pylint: disable=unused-variable

    x = 10
    y = 20
    z = 30
    print("Hello")
    ```

> [!TIP]
> To ignore multiple rules at once, separate them with commas:
>
> ```python
> # pylint: disable=unused-variable,missing-docstring
> x = 10
> y = "hello"
> # pylint: enable=unused-variable,missing-docstring
> ```
>
>
> ```python
> # flake8: noqa: E203, F841
> x = 10 # unused variable catched by F841 directive
> y = [1, 2, 3 , 4] # unexepected extra space catched by E203 directive
> ```


### Ignoring Rules in Formatters

For tools like `black`, use `# fmt: off` and `# fmt: on` to ignore formatting in specific sections:

```python
# fmt: off
def messy_code(): print("Hello") # This won't be reformatted
# fmt: on
```


## Setting Rules Using Configuration Files

In the real-world, projects use global configuration files to set the rules for linting and formatting, for instance:


### Linting

- Using `flake8`:
    ```ini
    # ".flake8" file

    [flake8]
    # List of error and warning codes to ignore (comma-separated)
    # Examples:
    #   E203: Whitespace before ':'
    #   E266: Too many leading '#' for block comment
    #   E402: Module level import not at top of file
    #   E501: Line too long (handled by max-line-length below)
    #   W503: Line break occurred before a binary operator
    #   F403: 'from module import *' used; unable to detect undefined names
    #   F401: Module imported but unused
    #   F841: Local variable assigned but never used
    ignore = E203, E266, E402, , E501, W503, F403, F401, F841

    # Maximum allowed line length (overrides E501)
    max-line-length = 120

    # Files and directories to exclude from linting (comma-separated)
    # Common examples:
    #   .git: Git configuration and metadata
    #   __pycache__: Compiled Python files
    #   docs/source/conf.py: Documentation configuration file
    #   old, build, dist: Legacy or distribution directories
    exclude = .git,__pycache__,docs/source/conf.py,old,build,dist

    # Set a maximum Cyclomatic Complexity for functions and methods
    # This limits how complex a single function or method can be.
    max-complexity = 10

    # List of error and warning codes to enforce
    # Examples:
    #   B: Bugbear warnings
    #   C: Cyclomatic complexity
    #   E: Pycodestyle (formerly PEP 8) errors
    #   F: Pyflakes errors
    #   W: Pycodestyle warnings
    #   T4: flake8-bugbear specific checks
    #   B9: flake8-bandit specific checks
    select = B,C,E,F,W,T4,B9
    ```

- Using `pylint`:
    ```ini
    # ".pylintrc" file

    [MASTER]
    # Files or directories to ignore (comma-separated)
    ignore = .git,__pycache__,docs/source/conf.py,old,build,dist

    # Set maximum line length
    max-line-length = 120

    [MESSAGES CONTROL]
    # List of message IDs to disable
    #   C0114: Missing module docstring.
    #   C0115: Missing class docstring.
    #   C0116: Missing function or method docstring.
    #   W0511: TODO found.
    #   R0903: Too few public methods in a class.
    disable = C0114, C0115, C0116, W0511, R0903

    [DESIGN]
    # Set maximum number of attributes in a class
    max-attributes = 10

    # Set maximum allowable complexity for a function or method
    max-complexity = 10

    [FORMAT]
    # Set indentation style and size
    indent-string = "    "
    ```


### Formatting

Using `black`, it can be configured using a `pyproject.toml` file or a `.black` configuration file, but the most common and modern approach is to use the `[tool.black]` section within `pyproject.toml`.

```ini
# "pyproject.toml" file

[tool.black]
# Set the maximum allowed line length to 120 characters
line-length = 120

# Include files with the extension '.py' or '.pyi'
include = '\.pyi?$'

# Exclude specific directories or files from being formatted by Black
exclude = '''
/(
    # Exclude .git directory
    \.git

    # Exclude .hg directory (Mercurial repository)
  | \.hg

    # Exclude mypy cache
  | \.mypy_cache

    # Exclude tox environments
  | \.tox

    # Exclude virtual environments
  | \.venv

    # Exclude build directories
  | _build
  | buck-out
  | build
  | dist

    # Exclude blib2to3, which is used by Python 2-to-3 conversion
  | blib2to3

    # Exclude test data
  | tests/data
)/
'''
```


## Adding to a Pre-Commit Hook

To integrate these tools into a `Git pre-commit` workflow using the `pre-commit` library, follow these steps:


### Setup Pre-Commit

1. Install the `pre-commit` library:
   ```bash
   $ pip install pre-commit
   ```
2. Create a `.pre-commit-config.yaml` file in the root folder of your repository.


### Set the Rules for the Pre-Commit Hook

```yaml
repos:
  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: [--max-line-length=120]

  - repo: https://github.com/pre-commit/mirrors-pylint
    rev: v3.0.0
    hooks:
      - id: pylint
        args: ["--disable=C0114,C0116"]

  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black
        args: ["--line-length=88"]
```


### Using Pre-Commit

1. Install the hooks

    ```bash
    $ pre-commit install
    ```

2. Test the hooks on **ALL** files

    ```bash
    $ pre-commit run --all-files
    ```

After the `pre-commit` installation, all your commits will be checked before its completion.

> [!TIP]
> Skipping Pre-commit Hooks Temporarily, if needed
>
> Skip all the pre-commit hooks
> ```bash
> $ git commit -m "Your commit message" --no-verify
> ```
>
>
> Skip `Flake8` pre-commit hooks
> ```bash
> $ git commit -m "Your commit message # flake8: skip"
> ```
>
>
> Skip `Pylint` pre-commit hooks
> ```bash
> $ git commit -m "Your commit message # pylint: skip"
> ```
>
>
> Skip `Flake8` pre-commit hooks
> ```bash
> $ git commit -m "Your commit message # black: skip"
> ```

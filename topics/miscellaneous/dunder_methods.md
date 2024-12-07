# About Dunder Methods


## Dunder (Magic) Methods Are Public

1. Magic methods (aka Dunder - **D**ouble **UNDER**score - methods) are part of Python's core mechanics and are designed to be accessible by Python's interpreter and the user indirectly through operations.
2. They are intended to define or override default behaviors and are therefore inherently public, even though developers do not typically call them directly


## Why Use Double Underscores for Magic Methods?

The double underscores on both sides serve a different purpose:
- They prevent naming conflicts with user-defined methods or attributes.
- They highlight their special nature as methods tied to Python's internal functionality.


## Signify Special Behavior

Magic methods are not meant to be called directly by developers in typical use, instead, they are implicitly triggered by specific operations (e.g., calling `__str__` when `str()` is used, or `__add__` when the `+` operator is applied).

The naming helps developers recognize that these methods have specific purposes tied to Python's syntax and built-in functionality.


## Consistent Syntax

The double underscore convention provides a uniform way to identify these methods across Python. Whether it's object initialization (`__init__`), string representation (`__str__`), or operator overloading (`__add__`, `__eq__`), the naming pattern makes it clear that they belong to Python's internal mechanics.


## Historical Context

The double underscore style was introduced to Python early in its development to differentiate these **"magic"** methods as part of the language's core, while also giving developers flexibility to create their own methods without worrying about accidentally overriding or conflicting with built-in functionality.

# Section 2: Regular Expressions

Regular expressions (regex) are sequences of characters that define search patterns. They are used for string matching and manipulation. Python provides the `re` module to work with regular expressions.

## References:

1. [Regular Expressions: Regexes in Python - Part 1](https://realpython.com/regex-python/)
2. [Regular Expressions: Regexes in Python - Part 2](https://realpython.com/regex-python-part-2/)
3. [re — Regular expression operations - Python Documentation](https://docs.python.org/3/library/re.html)
4. [Regular Expression HOWTO - Python Documentation](https://docs.python.org/3/howto/regex.html#regex-howto)

---

Regular expressions are powerful tools for matching, searching, and manipulating text. They are widely used in data validation, parsing, and text processing. Now suppose you need to write Python code to find out whether a log record contains the substring 'HttpStatusCode: xxx' where http code can be any three consecutive decimal digit characters.

```python
log_record = "some text HttpStatusCode: 202 some text"
```

## 2.1 Using and Compiling Regular Expressions

To use regular expressions in Python, you need to import the `re` module. The `re.compile()` function is used to compile a regular expression pattern into a regex object.

### Syntax:
```python
import re
pattern = re.compile(pattern, flags=0)
```

### Example:
```python
import re
pattern = re.compile("HttpStatusCode: 202")
```

You can enable a case-insensitive mode that would let this RE match `HTTPSTATUSCODE` or `httpstatuscode` as well

## Example:
```python
import re
pattern = re.compile("HttpStatusCode: 202", re.IGNORECASE)
```

In this case, the <regex> pattern is just the plain string `HttpStatusCode: 202`. The pattern matching here is still just character-by-character comparison, pretty much the same as the `in` operator and `.find()` method.

## 2.2 Python Regex Metacharacters

The real power of regex matching in Python emerges when <regex> contains special characters called metacharacters. These have a unique meaning to the regex matching engine and vastly enhance the capability of the search.
Here’s a complete list of the metacharacters: `. ^ $ * + ? { } [ ] \ | ( )`. Please refer to provided links for Python Documentation to check their meanings.
Let's proceed with our example:
`\W`- matches any non-alphanumeric character.
`\s`- matches any whitespace character.
`\d`- matches any decimal digit.
`{m}`- specifies that exactly m copies of the previous RE should be matched.

The following metacharacter sequence will match any http status code

### Example:
```python
import re
pattern = re.compile("HttpStatusCode\W\s\d{3}", re.I)
```

Once you have an object representing a compiled regular expression, you can use it's methods and attributes.

[Note] If you want to match an arbitrary literal string that may have regular expression metacharacters in it,
you can use `re.escape(pattern)` function, which returns a copy of <regex> with each nonword character (anything other than a letter, digit, or underscore) preceded by a backslash.
It saves you the trouble of putting in all the backslash characters manually.

### Example:
```python
import re
re.escape('https://www.python.org') # Output: 'https://www\\.python\\.org'
```

## 2.3 Matching Patterns

The `match()` function checks for a match only at the beginning of the string.

### Syntax:
```python
result = pattern.match(string)
```
Return a match object instance if there is a successful match and `None` if no match can be found.

### Example:
```python
log_record = "HttpStatusCode: 202 some text"
pattern.match(log_record) # Output: <re.Match object; span=(0, 19), match='HttpStatusCode: 202'>
log_record = "some text HttpStatusCode: 202 some text"
pattern.match(log_record) # Output: None
```

## 2.4 Match Objects

Match objects always have a boolean value of `True`. You can test whether there was a match with a simple if statement:

### Syntax:
```python
match = pattern.match(string)
if match:
    pass
```

Match object instances also have several methods and attributes; the most important ones are:
- `group()`: Return the string matched by the RE
- `start()`: Return the starting position of the match
- `end()`: Return the ending position of the match
- `span()`: Return a tuple containing the (start, end) positions of the match

### Example:
```python
import re
m = re.match(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
m.group(1) # Output: foo
m.group(3) # Output: baz
```
[Note] You don’t have to create a pattern object and call its methods; here a module function `re.match(pattern, string)` was used which is equivalent to match object method that you have already seen.

## 2.5 Searching Patterns

`search()` checks for a match anywhere in the string and reports the first match it finds.

### Example:
```python
log_record = "HttpStatusCode: 202 some text"
pattern.search(log_record).span() # Output: (0, 19)
log_record = "some text HttpStatusCode: 202 some text"
pattern.search(log_record).span() # Output: (10, 29)
```

Regular expressions beginning with an anchor `^` can be used with `search()` to restrict the match at the beginning of the line:

### Example:
```python
log_record = "some text HttpStatusCode: 202 some text"
print(re.search("^HttpStatusCode\W\s\d{3}", log_record)) # Output: None
```

Refer Python Documentation to know nore about anchors.

## 2.6 Finding All Matches

`findall()` matches all occurrences of a pattern, not just the first one as `search()` does.

### Example:
```python
import re
print(re.findall("\d+","abc123def456"))  # Output: ['123', '456']
```

[Note] Here we used a new quantifier metacharacter `+`, which matches one or more repetitions of the preceding regex. You can find the full lists of quantifier metacharacters in the documentation.

## 2.7 Replacing Patterns

`sub()` find all substrings where the RE matches, and replace them with a different string.

### Syntax:
```python
re.sub(pattern, repl, string, count=0, flags=0)
```

### Example:
```python
import re
re.sub("\d+", "#", "abc123def456") # Output: abc#def#
re.sub("\d+", "#", "abc123def456", count=1) # Outut: abc#def456
```

## 2.8 Splitting Strings

`split()` splits string into substrings using <regex> as the delimiter and returns the substrings as a list. You can limit the number of splits made, by passing a non-zero value
for `maxsplit`; the remainder of the string is returned as the final element of the list.

### Syntax:
```python
re.split(pattern, string, maxsplit=0, flags=0)
```

### Example:
```python
re.split("\d+", "abc123def456") # Output: ['abc', 'def', '']
re.split("\d+", "abc123def456", maxsplit=1) # Outut: ['abc', 'def456']
```

### Practical Exercises (Drills):

1. Write a regex to match a valid email address.
2. Write a regex to find all words that start with a capital letter.
3. Write a regex to match a phone number in the format (123) 456-7890.
4. Write a regex to find all dates in the format DD/MM/YYYY.
5. Write a regex to match a URL.
6. [TI] Find a max number in a string: abc123def456

# String in Python

- [String in Python](#string-in-python)
  - [Python `str` Methods](#python-str-methods)
      - [Examples](#examples)
    - [**Why Strings Are Important**](#why-strings-are-important)

> A string in Python is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are one of the most fundamental data types in Python and are used to represent text.

- Here are some key points about strings:
    1. **Immutable**: Strings are immutable, meaning once a string is created, it cannot be changed. Any operation that modifies a string actually creates a new string.
    2. **Ordered**: Strings maintain the order of characters, meaning the sequence of characters is preserved.
    3. **Indexed**: Each character in a string has an index, starting from `0` for the first character. You can access characters using their index.
    4. **Iterable**: Strings can be iterated over using loops, just like lists.
    5. **Versatile**: Strings support a wide range of operations, such as slicing, concatenation, formatting, and more.

## Python `str` Methods

- **capitalize()**  
  Converts the first character to uppercase and the rest to lowercase.

- **casefold()**  
  Converts the string to lowercase, more aggressive than `lower()`.

- **center(width, fillchar=' ')**  
  Centers the string within a given width using a fill character.

- **count(substring)**  
  Returns the number of times a substring appears in the string.

- **encode(encoding='utf-8')**  
  Encodes the string into bytes using the specified encoding.

- **endswith(suffix)**  
  Returns `True` if the string ends with the specified suffix.

- **expandtabs(tabsize=8)**  
  Replaces tab characters (`\t`) with spaces.

- **find(substring)**  
  Returns the lowest index of the substring, or -1 if not found.

- **format(**kwargs)**  
  Inserts values into placeholders in a string.

- **format_map(mapping)**  
  Similar to `format()`, but uses a dictionary for substitution.

- **index(substring)**  
  Like `find()`, but raises an error if the substring is not found.

- **isalnum()**  
  Returns `True` if all characters are alphanumeric.

- **isalpha()**  
  Returns `True` if all characters are letters.

- **isascii()**  
  Returns `True` if all characters are ASCII.

- **isdecimal()**  
  Returns `True` if all characters are decimal numbers.

- **isdigit()**  
  Returns `True` if all characters are digits.

- **isidentifier()**  
  Returns `True` if the string is a valid Python identifier.

- **islower()**  
  Returns `True` if all characters are lowercase.

- **isnumeric()**  
  Returns `True` if all characters are numeric.

- **isprintable()**  
  Returns `True` if all characters are printable.

- **isspace()**  
  Returns `True` if all characters are whitespace.

- **istitle()**  
  Returns `True` if the string is in title case.

- **isupper()**  
  Returns `True` if all characters are uppercase.

- **join(iterable)**  
  Joins elements of an iterable with the string as separator.

- **ljust(width, fillchar=' ')**  
  Left-justifies the string in a field of given width.

- **lower()**  
  Converts all characters to lowercase.

- **lstrip()**  
  Removes leading whitespace (or characters).

- **maketrans()**  
  Creates a mapping table for `translate()`.

- **partition(sep)**  
  Splits the string into three parts: before, separator, after.

- **removeprefix(prefix)**  
  Removes the prefix if the string starts with it.

- **removesuffix(suffix)**  
  Removes the suffix if the string ends with it.

- **replace(old, new)**  
  Replaces all occurrences of a substring with another.

- **rfind(substring)**  
  Returns the highest index of the substring, or -1 if not found.

- **rindex(substring)**  
  Like `rfind()`, but raises an error if the substring is not found.

- **rjust(width, fillchar=' ')**  
  Right-justifies the string in a field of given width.

- **rpartition(sep)**  
  Like `partition()` but searches from the right.

- **rsplit(sep=None, maxsplit=-1)**  
  Splits the string from the right.

- **rstrip()**  
  Removes trailing whitespace (or characters).

- **split(sep=None, maxsplit=-1)**  
  Splits the string into a list using a separator.

- **splitlines()**  
  Splits the string at line breaks.

- **startswith(prefix)**  
  Returns `True` if the string starts with the specified prefix.

- **strip()**  
  Removes leading and trailing whitespace (or characters).

- **swapcase()**  
  Swaps uppercase to lowercase and vice versa.

- **title()**  
  Converts the string to title case.

- **translate(mapping)**  
  Replaces characters based on a translation table.

- **upper()**  
  Converts all characters to uppercase.

- **zfill(width)**  
  Pads the string with zeros on the left to fill the width.

#### Examples

```python
s = "hello world"

# capitalize
print(s.capitalize())  # Hello world

# casefold
print("HELLO".casefold())  # hello

# center
print("hi".center(10, '-'))  # ----hi----

# count
print("banana".count("a"))  # 3

# encode
print("hello".encode())  # b'hello'

# endswith
print("test.py".endswith(".py"))  # True

# expandtabs
print("a\tb\tc".expandtabs(4))  # a   b   c

# find
print("hello".find("e"))  # 1

# format
print("Hello, {}!".format("Alice"))  # Hello, Alice!

# format_map
print("Age: {age}".format_map({"age": 30}))  # Age: 30

# index
print("hello".index("e"))  # 1

# isalnum
print("abc123".isalnum())  # True

# isalpha
print("abc".isalpha())  # True

# isascii
print("abc".isascii())  # True

# isdecimal
print("123".isdecimal())  # True

# isdigit
print("123".isdigit())  # True

# isidentifier
print("var_1".isidentifier())  # True

# islower
print("hello".islower())  # True

# isnumeric
print("123".isnumeric())  # True

# isprintable
print("Hello!".isprintable())  # True

# isspace
print("   ".isspace())  # True

# istitle
print("Hello World".istitle())  # True

# isupper
print("HELLO".isupper())  # True

# join
print(",".join(["a", "b", "c"]))  # a,b,c

# ljust
print("hi".ljust(5, "."))  # hi...

# lower
print("HELLO".lower())  # hello

# lstrip
print("   test".lstrip())  # test

# maketrans & translate
trans = str.maketrans("abc", "123")
print("abc".translate(trans))  # 123

# partition
print("key:value".partition(":"))  # ('key', ':', 'value')

# removeprefix
print("TestHook".removeprefix("Test"))  # Hook

# removesuffix
print("misc.txt".removesuffix(".txt"))  # misc

# replace
print("one one one".replace("one", "two"))  # two two two

# rfind
print("banana".rfind("a"))  # 5

# rindex
print("banana".rindex("a"))  # 5

# rjust
print("hi".rjust(5, "."))  # ...hi

# rpartition
print("key:value".rpartition(":"))  # ('key', ':', 'value')

# rsplit
print("a,b,c".rsplit(",", 1))  # ['a,b', 'c']

# rstrip
print("test   ".rstrip())  # test

# split
print("a,b,c".split(","))  # ['a', 'b', 'c']

# splitlines
print("a\nb\nc".splitlines())  # ['a', 'b', 'c']

# startswith
print("hello.py".startswith("hello"))  # True

# strip
print("  test  ".strip())  # test

# swapcase
print("Hello".swapcase())  # hELLO

# title
print("hello world".title())  # Hello World

# upper
print("hello".upper())  # HELLO

# zfill
print("42".zfill(5))  # 00042
```

### **Why Strings Are Important**

Strings are essential in Python because they are used to represent and manipulate text data. They are widely used in tasks like:

- Input/output operations.
- Data processing and cleaning.
- Text analysis and natural language processing.
- Web development (e.g., handling URLs, HTML, JSON).

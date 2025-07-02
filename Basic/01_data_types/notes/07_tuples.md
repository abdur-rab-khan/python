# Tuples in Python

- [Tuples in Python](#tuples-in-python)
  - [Python Sequence Methods (`count`, `index`)](#python-sequence-methods-count-index)
    - [Examples](#examples)
  - [**Why Tuples Are Important**](#why-tuples-are-important)
  - [**Comparison with Lists**](#comparison-with-lists)
  - [**When to Use Tuples**](#when-to-use-tuples)

> A **tuple** in Python is a built-in data structure that stores an **ordered and immutable** sequence of elements. \
> Tuples are similar to lists, but they cannot be modified after creation.

- Here are some key points about tuples:
    1. **Ordered**: Tuples maintain the order of elements, meaning the items are stored in the sequence they are added.
    2. **Immutable**: Tuples are immutable, meaning once a tuple is created, it cannot be changed. You cannot add, remove, or modify elements.
    3. **Heterogeneous**: Tuples can store elements of different data types (e.g., integers, strings, floats, or even other tuples).
    4. **Indexed**: Each element in a tuple has an index, starting from `0` for the first element. You can access elements using their index.
    5. **Iterable**: Tuples can be iterated over using loops, just like lists.
    6. **Hashable**: Tuples are hashable (if all their elements are hashable), which means they can be used as keys in dictionaries or elements in sets.

## Python Sequence Methods (`count`, `index`)

- **count(x)**  
  Returns the number of times `x` appears in the list or tuple.

- **index(x[, start[, end]])**  
  Returns the index of the first occurrence of `x`. Raises an error if not found. Optional `start` and `end` define the search range.

### Examples

```python
# count() example with list
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # 3

# count() example with tuple
values = ('a', 'b', 'a', 'c')
print(values.count('a'))  # 2

# index() example with list
names = ['Alice', 'Bob', 'Charlie']
print(names.index('Bob'))  # 1

# index() with start and end
letters = ['a', 'b', 'c', 'b', 'd']
print(letters.index('b', 2))  # 3

# index() example with tuple
data = (10, 20, 30, 20)
print(data.index(20))  # 1
```

## **Why Tuples Are Important**

Tuples are essential in Python because:

- They are **immutable**, making them safer for storing data that should not change.
- They are **hashable**, so they can be used as keys in dictionaries or elements in sets.
- They are **memory-efficient** compared to lists for fixed-size data.
- They are commonly used for **returning multiple values from functions**.

## **Comparison with Lists**

- **Lists**: Ordered, mutable, allows duplicates, accessed by index.
- **Tuples**: Ordered, immutable, allows duplicates, accessed by index.

## **When to Use Tuples**

- When you want to ensure the data cannot be modified (e.g., constants, configuration settings).
- When you need to use a sequence as a dictionary key or set element.
- When returning multiple values from a function.

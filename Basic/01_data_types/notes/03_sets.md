# Sets in Python

- [Sets in Python](#sets-in-python)
  - [Python `set` Methods](#python-set-methods)
    - [Examples](#examples)
  - [Why sets are important](#why-sets-are-important)
  - [**Comparison with Lists, Dictionaries, and Strings**](#comparison-with-lists-dictionaries-and-strings)

> A set in Python is a built-in data structure that stores a collection of unique and unordered elements. \
> Sets are particularly useful when you need to ensure that there are no duplicate values and when you want to perform mathematical set operations like union, intersection, and difference.

- Here are some key points about sets
    1. **Unordered:** Sets do not maintain the order of elements, meaning the items are stored in an arbitrary order.
    2. **Mutable:** Sets are mutable, so you can add or remove elements after creation.
    3. **Unique Elements:** Sets automatically eliminate duplicate values. Each element in a set must be unique.
    4. **Un-Indexed:** Sets do not support indexing or slicing because they are unordered.
    5. **Heterogeneous:** Sets can store elements of different data types (e.g., integers, strings, floats), but the elements must be immutable (e.g., numbers, strings, tuples).
    6. **Efficient Membership Testing:** Sets are optimized for checking whether an element is present in the set, making them faster than lists for this purpose.

## Python `set` Methods

- **add(elem)**  
  Adds an element `elem` to the set if it is not already present.

- **clear()**  
  Removes all elements from the set, making it empty.

- **copy()**  
  Returns a shallow copy of the set.

- **difference(*sets)**  
  Returns a new set with elements that are only in the original set and not in the given sets.

- **difference_update(*sets)**  
  Removes elements from the set that are present in the given sets.

- **discard(elem)**  
  Removes `elem` from the set if it is present. Does nothing if not found.

- **intersection(*sets)**  
  Returns a new set with elements that are common to all given sets.

- **intersection_update(*sets)**  
  Updates the set to keep only elements found in all given sets.

- **isdisjoint(other_set)**  
  Returns `True` if the set has no elements in common with `other_set`.

- **issubset(other_set)**  
  Returns `True` if all elements of the set are in `other_set`.

- **issuperset(other_set)**  
  Returns `True` if all elements of `other_set` are in the set.

- **pop()**  
  Removes and returns an arbitrary element from the set. Raises error if the set is empty.

- **remove(elem)**  
  Removes `elem` from the set. Raises error if `elem` is not found.

- **symmetric_difference(other_set)**  
  Returns a new set with elements in either the set or `other_set` but not both.

- **symmetric_difference_update(other_set)**  
  Updates the set to keep only elements that are in either the set or `other_set` but not both.

- **union(*sets)**  
  Returns a new set with all elements from the set and the given sets (no duplicates).

- **update(*sets)**  
  Adds all elements from the given sets to the set (like union but in-place).

### Examples

```python
# add()
s = {1, 2}
s.add(3)  # s becomes {1, 2, 3}

# clear()
s = {1, 2, 3}
s.clear()  # s becomes set()

# copy()
s = {1, 2, 3}
new_s = s.copy()  # new_s is {1, 2, 3}

# difference()
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))  # {1, 3}

# difference_update()
a = {1, 2, 3}
b = {2, 4}
a.difference_update(b)  # a becomes {1, 3}

# discard()
s = {1, 2}
s.discard(2)  # s becomes {1}
s.discard(5)  # no error, s stays {1}

# intersection()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}

# intersection_update()
a = {1, 2, 3}
b = {2, 4}
a.intersection_update(b)  # a becomes {2}

# isdisjoint()
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True

# issubset()
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

# issuperset()
a = {1, 2, 3}
b = {2}
print(a.issuperset(b))  # True

# pop()
s = {1, 2, 3}
s.pop()  # removes a random element

# remove()
s = {1, 2}
s.remove(2)  # s becomes {1}
# s.remove(5)  # would raise KeyError

# symmetric_difference()
a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))  # {1, 2, 4}

# symmetric_difference_update()
a = {1, 2, 3}
b = {2, 4}
a.symmetric_difference_update(b)  # a becomes {1, 3, 4}

# union()
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# update()
a = {1}
b = {2, 3}
a.update(b)  # a becomes {1, 2, 3}

```

## Why sets are important

- Sets are essential in Python because they:
  - Ensure uniqueness of elements, which is useful for tasks like removing duplicates from a list.
  - Provide efficient membership testing, making them faster than lists for this purpose.
  - Support mathematical set operations, which are useful in data analysis and algorithm design.

## **Comparison with Lists, Dictionaries, and Strings**

- **Lists**: Ordered, mutable, allows duplicates, accessed by index.
- **Dictionaries**: Key-value pairs, unordered (before Python 3.7), mutable, accessed by keys.
- **Strings**: Ordered, immutable, sequence of characters, accessed by index.
- **Sets**: Unordered, mutable, unique elements, no indexing.
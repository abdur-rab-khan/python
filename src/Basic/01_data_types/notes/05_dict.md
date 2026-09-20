# Dictionary in Python

- [Dictionary in Python](#dictionary-in-python)
  - [Python `dict` Methods (Sorted by Most Common)](#python-dict-methods-sorted-by-most-common)
    - [Examples](#examples)
  - [**Why Dictionaries Are Important**](#why-dictionaries-are-important)

> A **dictionary** in Python is a built-in data structure that stores data in **key-value pairs**. \
> It is one of the most powerful and commonly used data types in Python because of its efficiency in storing and retrieving data.

- Here are some key points about dictionaries
    1. **Key-Value Pairs**: Each element in a dictionary consists of a **key** and its corresponding **value**. The key acts as a unique identifier for the value.
    2. **Unordered (Before Python 3.7)**: Before Python 3.7, dictionaries were unordered, meaning the elements were not stored in any specific order. Starting from Python 3.7, dictionaries maintain insertion order.
    3. **Mutable**: Like lists, dictionaries are mutable, so you can add, remove, or modify key-value pairs after creation.
    4. **Keys Must Be Unique and Immutable**: Dictionary keys must be unique and of an immutable data type (e.g., strings, integers, or tuples). Values can be of any data type.
    5. **Fast Lookups**: Dictionaries are optimized for fast lookups. Retrieving a value using its key is very efficient, even for large datasets.

## Python `dict` Methods (Sorted by Most Common)

- **get(key, default=None)**  
  Returns the value for `key` if it exists; otherwise, returns `default`.

- **update(other_dict)**  
  Updates the dictionary with key-value pairs from another dictionary.

- **items()**  
  Returns a view of the dictionary’s key-value pairs.

- **keys()**  
  Returns a view of the dictionary’s keys.

- **values()**  
  Returns a view of the dictionary’s values.

- **copy()**  
  Returns a shallow copy of the dictionary.

- **pop(key[, default])**  
  Removes the specified key and returns its value. If key is not found, returns `default` if provided, otherwise raises an error.

- **popitem()**  
  Removes and returns the last inserted key-value pair.

- **setdefault(key, default=None)**  
  Returns the value of `key` if it exists. If not, inserts `key` with `default` as value and returns `default`.

- **clear()**  
  Removes all items from the dictionary.

- **fromkeys(iterable, value=None)**  
  Creates a new dictionary from the given iterable, using the same value for all keys.

### Examples

```python
# get()
person = {"name": "Alice", "age": 30}
print(person.get("name"))         # Alice
print(person.get("gender", "N/A"))  # N/A

# update()
person.update({"age": 31, "city": "New York"})  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# items()
print(person.items())  # dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')])

# keys()
print(person.keys())  # dict_keys(['name', 'age', 'city'])

# values()
print(person.values())  # dict_values(['Alice', 31, 'New York'])

# copy()
copy_person = person.copy()  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# pop()
age = person.pop("age")  # 31, person becomes {'name': 'Alice', 'city': 'New York'}

# popitem()
last_item = person.popitem()  # removes ('city', 'New York')

# setdefault()
person.setdefault("gender", "Female")  # Adds 'gender': 'Female' if not present

# clear()
person.clear()  # {}

# fromkeys()
defaults = dict.fromkeys(["id", "role"], "unknown")  # {'id': 'unknown', 'role': 'unknown'}
```

## **Why Dictionaries Are Important**

Dictionaries are essential in Python because they allow you to store and retrieve data efficiently using keys. They are widely used in tasks like:

- Storing configuration settings.
- Representing JSON-like data structures.
- Counting occurrences of items (e.g., word frequency in a text).
- Caching results for quick lookup.

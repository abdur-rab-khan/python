# List in Python

> A **list** in Python is a built-in data structure that is used to store a collection of items. \
> It is one of the most commonly used data types in Python because of its flexibility and versatility.

- Here are some key points about lists
    1. **Ordered Collection**: Lists maintain the order of elements, meaning the items are stored in the sequence they are added.
    2. **Mutable**: Lists are mutable, which means you can modify them after creation. You can add, remove, or change elements.
    3. **Heterogeneous**: Lists can store elements of different data types (e.g., integers, strings, floats, or even other lists).
    4. **Indexed**: Each element in a list has an index, starting from `0` for the first element. You can access elements using their index.
    5. **Dynamic**: Lists can grow or shrink in size as needed.

## Python `list` Methods (Sorted by Most Common)

- **append(x)**  
  Adds an item `x` to the end of the list.

- **extend(iterable)**  
  Adds all items from another iterable to the end of the list.

- **insert(index, x)**  
  Inserts item `x` at a specified index.

- **remove(x)**  
  Removes the first occurrence of item `x`.

- **pop(index=-1)**  
  Removes and returns the item at the given index. Defaults to the last item.

- **clear()**  
  Removes all items from the list.

- **copy()**  
  Returns a shallow copy of the list.

- **count(x)**  
  Returns the number of times `x` appears in the list.

- **index(x)**  
  Returns the index of the first occurrence of `x`.

- **reverse()**  
  Reverses the elements of the list in place.

- **sort(key=None, reverse=False)**  
  Sorts the list in ascending order by default. Can sort with custom keys and reverse.

### Examples

```python
# len(list)
lst = [1,2,3]
print(len(lst)) # 3

# append()
lst = [1, 2]
lst.append(3)  # [1, 2, 3]

# extend()
lst = [1, 2]
lst.extend([3, 4])  # [1, 2, 3, 4]

# insert()
lst = [1, 3]
lst.insert(1, 2)  # [1, 2, 3]

# remove()
lst = [1, 2, 3, 2]
lst.remove(2)  # [1, 3, 2] (removes first 2)

# pop()
lst = [1, 2, 3]
lst.pop()  # 3, lst becomes [1, 2]
lst.pop(0)  # 1, lst becomes [2]

# clear()
lst = [1, 2, 3]
lst.clear()  # []

# copy()
original = [1, 2, 3]
copied = original.copy()  # [1, 2, 3]

# count()
lst = [1, 2, 2, 3]
print(lst.count(2))  # 2

# index()
lst = [10, 20, 30]
print(lst.index(20))  # 1

# reverse()
lst = [1, 2, 3]
lst.reverse()  # [3, 2, 1]

# sort()
lst = [3, 1, 2]
lst.sort()  # [1, 2, 3]
lst.sort(reverse=True)  # [3, 2, 1]
```

## **Why Lists Are Important**

Lists are fundamental in Python because they allow you to store and manipulate collections of data efficiently. They are widely used in tasks like data processing, algorithm implementation, and more.

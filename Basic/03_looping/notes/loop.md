# Looping in Python

- [Looping in Python](#looping-in-python)
  - [`for` Loop](#for-loop)
    - [Example](#example)
    - [Output](#output)
    - [Looping with `range()`](#looping-with-range)
    - [Output](#output-1)
    - [Looping with `enumerate()`](#looping-with-enumerate)
    - [Output](#output-2)
    - [Looping with `zip()`](#looping-with-zip)
    - [Output](#output-3)
    - [Looping with `break` and `continue`](#looping-with-break-and-continue)
    - [Output](#output-4)
    - [Looping with `List Comprehensions`](#looping-with-list-comprehensions)
    - [Output](#output-5)
  - [`while` Loop](#while-loop)
    - [Example](#example-1)
    - [Output](#output-6)


> **Looping** in Python is used to repeatedly execute a block of code as long as a certain condition is met. \
> Loops are essential for automating repetitive tasks and iterating over sequences like lists, strings, or ranges.

- Python provides two main types of loops
- **`for` loop**: Used for iterating over a sequence (like a list, tuple, or string) or other iterable objects.
- **`while` loop**: Repeats a block of code as long as a specified condition is true.

## `for` Loop

```python
# Syntax
for variable in iterable:
    # Code block to execute
```

### Example

```python
# Using a for loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Output

```shell
apple
banana
cherry
```

### Looping with `range()`

You can also use the `range()` function to generate a sequence of numbers, which is often used with a `for` loop.

```python
# Using range() to loop through numbers
for i in range(1, 6):
    print(i)
```

### Output

```shell
1
2
3
4
5
```

### Looping with `enumerate()`
The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object

```python
# Using enumerate() to get index and value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
```

### Output

```shell
Index: 0, Fruit: apple
Index: 1, Fruit: banana
Index: 2, Fruit: cherry
```

### Looping with `zip()`

The `zip()` function combines two or more iterables (like lists or tuples) into a single iterable of tuples.

```python
# Using zip() to combine two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### Output

```shell
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

### Looping with `break` and `continue`

- You can control the flow of loops using `break` and `continue` statements.
    - **`break`**: Exits the loop prematurely.
    - **`continue`**: Skips the current iteration and continues with the next one.

```python
# Using break and continue in a loop

for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

### Output

```shell
1
3
```

### Looping with `List Comprehensions`

List comprehensions provide a concise way to create lists based on existing lists or other iterables.

```python

# Using list comprehension to create a new list
squares = [x**2 for x in range(1, 6)]
print(squares)

# Example 2 - With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
```

### Output

```shell
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10]
```

## `while` Loop

```python
# Syntax
while condition:
    # Code block to execute
```

### Example

```python
# Using a while loop to print numbers from 1 to 5
count = 1   

while count <= 5:
    print(count)
    count += 1
```

### Output

```shell
1
2
3
4
5
```
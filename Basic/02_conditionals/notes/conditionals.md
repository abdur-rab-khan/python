# Conditionals in Python

- [Conditionals in Python](#conditionals-in-python)
  - [🟦 Comparison Operators](#-comparison-operators)
  - [🟥 Logical Operators](#-logical-operators)
  - [🟩 Membership \& Identity Tests](#-membership--identity-tests)
    - [Membership Operators](#membership-operators)
    - [Identity Operators](#identity-operators)
  - [🟨 Operator Precedence](#-operator-precedence)
  - [🟪 Boolean Examples](#-boolean-examples)
  - [🟩 Basic If-Else Pattern](#-basic-if-else-pattern)
  - [🟧 Simple One-Liner Conditionals](#-simple-one-liner-conditionals)
  - [🟨 Pattern Matching (Python 3.10+)](#-pattern-matching-python-310)
  - [🟥 Comprehensions with Conditionals](#-comprehensions-with-conditionals)
  - [🟦 Boolean Shortcuts with Conditionals](#-boolean-shortcuts-with-conditionals)
  - [🟫 Nested Ternary with Readability](#-nested-ternary-with-readability)

> **Conditionals** in Python are used to make decisions in your code based on certain conditions. \
> They allow you to execute specific blocks of code only if a particular condition is met. \
> Python provides several constructs for implementing conditionals, including `if`, `elif`, and `else`.

## 🟦 Comparison Operators

Used to compare two values. Returns `True` or `False`.

| Operator | Description     | Example      | Result  |
|----------|------------------|--------------|---------|
| `==`     | Equal to         | `5 == 5`     | `True`  |
| `!=`     | Not equal to     | `5 != 3`     | `True`  |
| `>`      | Greater than     | `7 > 3`      | `True`  |
| `<`      | Less than        | `2 < 5`      | `True`  |
| `>=`     | Greater or equal | `5 >= 5`     | `True`  |
| `<=`     | Less or equal    | `4 <= 6`     | `True`  |

---

## 🟥 Logical Operators

Used to combine conditional statements.

| Operator | Description                    | Example              | Result   |
|----------|--------------------------------|----------------------|----------|
| `and`    | Returns `True` if both are true| `True and True`      | `True`   |
| `or`     | Returns `True` if one is true  | `True or False`      | `True`   |
| `not`    | Reverses the result            | `not True`           | `False`  |

---

## 🟩 Membership & Identity Tests

### Membership Operators

Check if a value exists in a sequence. these are commonly works with `dict`, `sets`, `tuples`, `dict`

| Operator | Example        | Result   |
|----------|----------------|----------|
| `in`     | `'a' in 'cat'` | `True`   |
| `not in` | `5 not in [1,2,3]` | `True`|

### Identity Operators

Check if two objects are the same (in memory).

| Operator | Example        | Result   |
|----------|----------------|----------|
| `is`     | `x is y`       | `True` if same object |
| `is not` | `x is not y`   | `True` if different objects |

---

## 🟨 Operator Precedence

Order in which Python evaluates operators.

| Expression             | Evaluated As              |
|------------------------|---------------------------|
| `3 + 2 > 4 and 5 < 10` | `True and True → True`    |

---

## 🟪 Boolean Examples

```python
x = 10
y = 5
print(x > y and y < 3)    # False
print(x == 10 or y == 10) # True

```

---

## 🟩 Basic If-Else Pattern

Use `if`, `elif`, and `else` to control the flow of logic.

```python
x = 10

if x > 5:
    print("Greater than 5")
elif x == 5:
    print("Equal to 5")
else:
    print("Less than 5")
```

---

## 🟧 Simple One-Liner Conditionals

A compact way to assign values using conditionals.

```python
x = 7
result = "Yes" if x > 5 else "No"
print(result)  # Yes
```

---

## 🟨 Pattern Matching (Python 3.10+)

Use match statements to handle multiple known cases.

```python
command = "start"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

---

## 🟥 Comprehensions with Conditionals

Use if/else inside list comprehensions.

```python
nums = [1, 2, 3, 4]
even_odd = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(even_odd)  # ['Odd', 'Even', 'Odd', 'Even']
```

---

## 🟦 Boolean Shortcuts with Conditionals

Use and and or for quick logic operations.

```python
x = 10

print(x > 5 and "Valid")    # Valid
print(x < 5 or "Default")   # Default
```

---

## 🟫 Nested Ternary with Readability

Ternary conditions can be nested but should be readable.

```python
x = 8

result = "High" if x > 10 else "Medium" if x > 5 else "Low"
print(result)  # Medium
```

# Function in Python

> A **`function**` in Python is a reusable block of code designed to perform a specific task. \
> Functions help organize code into logical, modular units, making it easier to read, debug, and maintain. \
> They promote code reusability and abstraction by allowing you to define a task once and execute it multiple times with different inputs

## **Key Characteristics of Functions**

1. **Reusability**: Functions can be called multiple times, reducing redundancy.
2. **Parameters and Arguments**: Functions accept inputs (parameters) and can return outputs (return values).
3. **Scope**: Variables inside a function are local to it unless declared as global.
4. **Modularity**: Functions break complex problems into smaller, manageable tasks.
5. **Built-in vs User-defined**: Python has built-in functions (e.g., `len()`, `print()`) and allows users to define custom functions.

## **Key Operations on Functions**

---

1. **Defining a Function**:

    ```python
    def greet(name):
        return f"Hello, {name}!"
    ```

2. **Calling a Function**:

    ```python
    message = greet("Alice")  # Output: "Hello, Alice!"
    ```

3. **Parameters vs. Arguments**:
    - **Parameters**: Variables listed in the function definition.
    - **Arguments**: Actual values passed to the function during a call.

    ```python
    def add(a, b):  # Parameters: a, b
        return a + b
    add(3, 5)       # Arguments: 3, 5 → returns 8
    ```

4. **Default Parameters**:

    Assign default values to parameters.

    ```python
    def power(base, exponent=2):
        return base ** exponent
    power(3)    # 3² = 9
    power(3, 3) # 3³ = 27
    ```

5. **Return Values**:

    A function can return any data type, including multiple values (as a tuple).

    ```python
    def min_max(numbers):
        return min(numbers), max(numbers)
    result = min_max([4, 2, 9])  # Returns (2, 9)
    ```

6. **Variable Scope**:
    - **Local Variables**: Defined inside a function (accessible only within it).
    - **Global Variables**: Defined outside a function (accessible globally using `global` keyword).

    ```python
    x = 10  # Global variable
    def update():
        global x
        x = 20  # Modifies the global x
    ```

7. **Lambda Functions**:

    Anonymous, single-expression functions defined with `lambda`.

    ```python
    square = lambda x: x ** 2
    print(square(5))  # Output: 25
    ```

8. **args and****kwargs**:
    - `args`: Accepts variable positional arguments as a tuple.
    - `*kwargs`: Accepts variable keyword arguments as a dictionary.

    ```python
    def display(*args, **kwargs):
        print("Positional:", args)
        print("Keyword:", kwargs)
    display(1, 2, name="Alice", age=25)
    ```

## **How Functions Work Internally in Memory**

Python functions are **first-class objects** (they can be assigned to variables, passed as arguments, etc.). Here’s how they work under the hood:

### **a. Function Objects**

---

- When you define a function, Python creates a **function object** in memory (e.g., `def foo(): ...` creates an object `foo`).
- This object contains:
  - The compiled bytecode of the function.
  - A reference to the global namespace where the function was defined.
  - Default argument values.
  - Closure variables (if any).

### **b. Execution Context**

---

- When a function is called, Python creates a **stack frame** (also called an activation record) to store:
  - Local variables.
  - Arguments passed to the function.
  - The return address (where to resume after the function call).
- The stack frame is destroyed when the function exits.

### **c. Closures and Memory**

---

- Variables captured by closures are stored in **cell objects**, which are referenced by both the outer and inner functions.
- These cells ensure the captured variables stay alive as long as the closure exists (even if the outer function’s frame is destroyed).

---

## Scopes in Python**


Scopes define the visibility and lifetime of variables. Python uses the **LEGB rule** to resolve variable names:

- **L (Local)**: Variables defined inside a function.
- **E (Enclosing)**: Variables in the local scope of enclosing functions (nested functions).
- **G (Global)**: Variables defined at the top level of a module or with `global`.
- **B (Built-in)**: Reserved names (e.g., `len`, `print`).

### **Example**

```python
x = 10  # Global scope

def outer():
    y = 20  # Enclosing scope
    def inner():
        z = 30  # Local scope
        print(x, y, z)  # LEGB: x (global), y (enclosing), z (local)
    inner()

outer()  # Output: 10 20 30
```

### **2. Closures**

---

A **closure** is a nested function that captures and "remembers" variables from its enclosing (non-global) scope, even after the outer function has finished executing. Closures are created when:

1. A nested function references a value from its enclosing scope.
2. The outer function returns the nested function.

```python
def maths(num):
    def sum(num2):
        return num + num2
    return sum

def maths2(num):
    def sum():
        return num + 10
    return sum()

print(maths(5)(55))
print(maths2(10))
```

### **How Closures Work**

- The inner function (`inner`) retains access to the variables of the outer function (`outer`) even after `outer` has completed execution.
- These variables are stored in the `__closure__` attribute of the closure function (as **cell objects**).

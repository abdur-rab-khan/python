"""
INNER WORKING OF THE PYTHON SCRIPT

Execution Flow:
Python Script → Interpreter → Bytecode → PVM → Execution

Step 1: Run the Script
- Command: python hello.py
- The Python interpreter reads the script (hello.py).

Step 2: Compile to Bytecode
- The script is compiled into bytecode (stored in .pyc files).
- Bytecode Basics:
  - Stored in .pyc files (frozen binary code).
  - Not human-readable and differs from machine code and source code.
  - Faster than source code as it is precompiled.
- Execution:
  - Bytecode is executed by the Python Virtual Machine (PVM).
  - .pyc files are used only for import statements, not for direct execution.

------------------ PYTHON VIRTUAL MACHINE (PVM) ------------------

Step 3: Python Virtual Machine (PVM)
- PVM Basics:
  - A stack-based virtual machine written in C.
  - Platform-independent and acts as the Python interpreter.
  - Reads bytecode and executes instructions, optimized for Python.
- PVM Responsibilities:
  - Manages memory, garbage collection, and exception handling.
  - Imports modules, executes functions, and runs scripts.
  - Executes bytecode instructions and manages the stack, heap, and code objects.
  - Handles the Global Interpreter Lock (GIL).
- Python Implementations:
  - CPython: Default implementation, written in C.
  - Other implementations: Jython, IronPython, PyPy, etc.

Step 4: Output
- The output is displayed on the screen.
- Generated by the print() function.
- Produced by the Python interpreter.

------------------- INTERPRETER VS COMPILER -------------------

Compiler:
- Reads source code and generates machine code (low-level program).
- Fast as it translates code in one go but harder to use due to compilation.
- Generates optimized machine code, ideal for performance-critical tasks.
- Used in static languages like C, C++, and Java.
- Generates standalone executables, great for production and large programs.
- Applications:
  - Embedded Systems, Game Development, Mobile Development, Desktop Development,
    Web Development, Cloud Development, Edge Development, Device Development,
    Server Development, Client Development, Browser Development, Robotics,
    Automation, Testing.

Interpreter:
- Reads source code and executes instructions (high-level program).
- Slow due to line-by-line execution but easy to use (no compilation needed).
- Great for debugging (real-time error display) and scripting (e.g., Python, Ruby, Perl).
- Ideal for prototyping, small programs, and interactive programming.
- Applications:
  - Web Development, Scientific Computing, Data Analysis, AI & Machine Learning,
    Deep Learning, Natural Language Processing, Computer Vision, Robotics,
    Automation, Testing.

------------------- PYTHON INTERNAL WORKING -------------------

Variable and Object Handling:
- When a variable is defined, it creates a reference to an object in memory.
- ref_count:
  - A counter that tracks the number of references to an object.
  - Incremented when a new reference is created; decremented when a reference is deleted.
  - Accessed using sys.getrefcount(), but it returns ref_count + 1 (due to temporary reference).
  - Example: import sys; x = 10; print(sys.getrefcount(x))
- Important Points:
  - Numbers and strings are treated as objects in Python.
  - When a variable is dereferenced, the reference is deleted, not the data.
  - Example: a = 5; a = a + 5 → Creates a new object (10) and updates the reference.

Mutable and Immutable:
● Mutable: The value of the object can be changed. Like list, dict, set, etc.
  📌 Suppose we create a list called a = [1, 2, 4], and we assign the value of the list to another variable called b = a. If we change the value of the list a,
  then the value of the list b will also be changed because the list is mutable. The list is stored in memory with a reference, so changes to a affect b.
  Example:
    a = [1, 2, 3, 4]
    b = a
    a[0] = 11

  --------------- VISUAL REPRESENTATION ---------------

  Stack Memory: Before changing the value of the list a
  +------------+-----------------+
  | Variable   | Memory Address  |
  +------------+-----------------+
  | a          | 0x1001          |  --> 0x2001 (Heap Memory)
  | b          | 0x1002          |  --> 0x2001 (Heap Memory)
  +------------+-----------------+

  Heap Memory:
  +------------+-----------------+
  | Address    | Value           |
  +------------+-----------------+
  | 0x2001     | [1, 2, 3, 4]    |
  +------------+-----------------+

  Stack Memory: After changing the value of the list a
  +------------+-----------------+
  | Variable   | Memory Address  |
  +------------+-----------------+
  | a          | 0x1001          |  --> 0x2001 (Heap Memory)
  | b          | 0x1002          |  --> 0x2001 (Heap Memory)
  +------------+-----------------+

  Heap Memory:
  +------------+-----------------+
  | Address    | Value           |
  +------------+-----------------+
  | 0x2001     | [11, 2, 3, 4]   |
  +------------+-----------------+

● Immutable: The value of the object cannot be changed. Like numbers, strings, tuples, etc.
  📌 Suppose we create a number called a = 5, and we assign the value of the number to another variable called b = a. If we change the value of the number a,
  then the value of the number b will not be changed because the number is immutable. The number is stored in memory with a reference, so changes to a do not affect b.
  After some time, if there are no references to the object, it will be deleted from memory by the garbage collector.
  Example:
    a = 5
    b = a
    a = 10

  --------------- VISUAL REPRESENTATION ---------------

  Step 1: a = 5
  Stack Memory:
  +------------+-----------------+
  | Variable   | Memory Address  |
  +------------+-----------------+
  | a          | 0x1001          |  --> 0x2001 (Heap Memory)
  +------------+-----------------+

  Heap Memory:
  +------------+-----------------+
  | Address    | Value           |
  +------------+-----------------+
  | 0x2001     | 5               |
  +------------+-----------------+

  Step 2: b = a
  Stack Memory:
  +------------+-----------------+
  | Variable   | Memory Address  |
  +------------+-----------------+
  | a          | 0x1001          |  --> 0x2001 (Heap Memory)
  | b          | 0x1002          |  --> 0x2001 (Heap Memory)
  +------------+-----------------+

  Heap Memory:
  +------------+-----------------+
  | Address    | Value           |
  +------------+-----------------+
  | 0x2001     | 5               |
  +------------+-----------------+

  Step 3: a = 10
  Stack Memory:
  +------------+-----------------+
  | Variable   | Memory Address  |
  +------------+-----------------+
  | a          | 0x1001          |  --> 0x2002 (Heap Memory)
  | b          | 0x1002          |  --> 0x2001 (Heap Memory)
  +------------+-----------------+

  Heap Memory:
  +------------+-----------------+
  | Address    | Value           |
  +------------+-----------------+
  | 0x2001     | 5               |
  | 0x2002     | 10              |
  +------------+-----------------+
"""

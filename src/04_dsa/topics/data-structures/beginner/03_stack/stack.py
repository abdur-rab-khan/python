# 🟡 Stack implementation using different methods.

# virtual IStack(int size) = 0; ❌ Wrong because, IStack  is called with

# object is created but for "ABSTRACT CLASS" no object will created. 1️⃣.

# Member function can be a virtual function 2️⃣. Destructure can be a virtual

# 3️⃣. Constructor ❌

# 4️⃣. Member variables ❌

# 👉 To understand why, Because abstract class is for creating a blueprint,

# like what member function will be there. There we only add things which are

# required in the main class.

# 👉 "Virtual: " Actually "virtual" keyword in C++, that tell C++ compiler

# don't decide that will run instead decide on run time.

# 👉 Enforce "= 0", We should have to implement this on "main" class, but

# it's not a case with "DESTRUCTURE" because even if you aren't define, C++

# compiler will automatically create this. 👉 Which is bad sometimes, Like

# suppose we are creating dynamic object, 100% will going to need a

# ""DESTRUCTURE"" for cleaning things.

# Pure virtual destructors still need a definition for the linker.

# 1️⃣. Let's implement "stack" using array DATA STRUCTURE.

# 2️⃣. Let's implement "stack" using VECTOR.

# 3️⃣. "main" function

# s1.push(12); ❌ Error: STACK OVERFLOW

# 12

# 3️⃣. Let's use build-in "Stack" from stl

# "Push" is used to add element at the top

# Tell's whether stack is empty or not.

# Gives the size of stack.

# Gives the top element of the stack.

# Remove top element from the top

# Stack supports two types of "underlying container" where they actually

# store the data. And we can change them manually, First element of "STACK

# CONSTRUCTOR" is the "underlying container". By default, ""UNDERLYING

# CONTAINER IS DEQUEUE"".

# Let's use list as a underlying container

# Let's use vector as a underlying container

# namespace StackDS

# 🟡 Different types of Stacks

""" 2️⃣. Monotonic Stack
        * In normal stack, there is no rule while pushing the element into the stack, but in monotonic stack there is a rule for pushing onto the stack.

        * 🟡 Types of Monotonic Stack
            * 1️⃣. Increasing Stack: In this case, If current element is greater than elements inside stack then we'll remove every elements smaller than current one, but if current element is smaller we push like in normal stack.
            * 2️⃣. Decreasing Stack: In this case, If current element is smaller than elements inside stack than we'll remove every elements greater than current one, but if current element is greater than we push like in normal stack.
 """

# Remove smaller from top

# Remove smaller from top

""" 3️⃣. Min/Max Stack
        * In normal stack, there is no rule while pushing the element into the stack, but in min/max stack there is a rule for pushing onto the stack.

        * 🟡 Types of min/max Stack
            * 1️⃣. min Stack: In this case, If current element is greater than top elements inside stack, than instead of pushing current element we push ""current top element"", but if current one is smaller than we push like in normal stack.
            * 2️⃣. max Stack: In this case, If current element is smaller than top elements inside stack, than instead of pushing current element we push ""current top element"", but if current one is greater than we push like in normal stack.
 """

# 4️⃣. Two Stacks

# 2️⃣. Monotonic Stack

# Now all the previous small elements will be removed.

# 4️⃣. Two Stacks

# namespace TypesOfStack

# StackDS::main();

class Stack:
    def __init__(self):
        self._items = []
    def push(self, value):
        self._items.append(value)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    def is_empty(self):
        return not self._items
    def size(self):
        return len(self._items)

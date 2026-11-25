"""
🟡 In Python, name lookup normally follows 4 scopes (LEGB):
    1. Local Scope
    2. Enclosing Scope
    3. Global Scope
    4. Built-in Scope

🟡 Each scope has its own lifetime.

1. Local Scope:
    * A local namespace is created when a function is called.
    * Variables created inside the function are normally stored in that
      function's local namespace.
    * The local namespace normally goes away after the function finishes.
    * We can read a global variable from a function, but assigning to that
      name normally creates a new local variable.
    * To modify the global variable, we use the "global" keyword.

2. Enclosing Scope:
    * This is the scope of an outer function when another function is
      defined inside it.
    * The inner function can read variables from the outer function.
    * To modify a variable from the enclosing function, we use the
      "nonlocal" keyword.
    * The enclosing variable can remain available after the outer function
      finishes if the inner function keeps a reference to it (closure).

3. Global Scope:
    * A module gets a global namespace when it is loaded/executed.
    * Names created at the module level are normally stored in the
      module's global namespace.
    * Functions can read global variables.
    * To assign to a global variable from inside a function, use "global".

4. Built-in Scope:
    * Contains names provided by Python's built-in namespace.
    * Examples: "print", "len", "abs", "int", "str", etc.
    * It is created when the Python interpreter starts and remains available
      while the interpreter is running.

🟡 NOTE:
    * A namespace is a mapping of names → objects.
    * Scopes determine where Python looks for a name when it is used directly.
    * Namespaces are commonly implemented using dictionaries, but a scope
      itself is not simply a dictionary.
"""

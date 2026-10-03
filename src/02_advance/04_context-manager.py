"""
🟡 A context manager in Python is useful to set up a resource and always release it when we are done, even if an error happens. We use it with the "with" keyword. The class needs two special methods: "__enter__", which runs when the with block starts (its return value goes into the name after "as"), and "__exit__", which runs when the with block finishes, or when an error happens inside it.
"""


class ContextManager:
    def __enter__(self):
        print("Lock")
        return self  # this goes into "c" below

    def __exit__(self, exc_type, exc_value, traceback):
        print("Release")
        return False  # do not hide errors


with ContextManager() as c:
    print("Working inside the block")

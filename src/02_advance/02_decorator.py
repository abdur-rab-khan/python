"""
🟡 A decorator is a function that takes another function as an argument and returns a function. It can return the same function, or a new function that wraps it.
🟡 A Python decorator is just "syntactic sugar" for something we can do by hand. When we write @wrapperFn above a function, Python automatically passes that function to wrapperFn. So @wrapperFn above def innerFun is the same as innerFun = wrapperFn(innerFun). After that, we can add any extra work we need.
🟡 The decorator must return a function, because after decoration the name innerFun points to whatever the decorator returned. So when we call innerFun(), we are calling the returned function. wrapperFn itself runs only once, at the time of decoration.

🔵 Simple wrapper function that takes a function and call that function directly.
def wrapperFn(fn):
    print(f"Trying to call {fn.__name__} function")
    fn()

def innerFun():
    print("This is inner function")

wrapperFn(innerFun)

🔵 What if, we want to pass arguments as well to the fn, we get the arguments we must have to return a function, that only took arguments and pass to fn.
def wrapperFn(fn):
    print(f"Trying to call {fn.__name__} function")

    def cb(*args):
        fn(*args)

    return cb

def innerFun(name):
    print(f"Hello {name}!")

fn = wrapperFn(innerFun)
fn("Python")
"""

# <---------------------------------> 🟡 DECORATOR WITHOUT ARGUMENTS <--------------------------------->

# 👉 Creating simple decorator function that takes a function as an argument and return that fn after printing these name
from collections.abc import Callable
from functools import wraps


def log(fn):
    print(f"Trying to call {fn.__name__}")
    return fn


@log
def cb():
    print("Inner function")


cb()

# <---------------------------------> 🟡 DECORATOR AND FN ARGUMENTS <--------------------------------->


# 👉 Creating another decorator that takes a function along with arguments and call the fn directly into the decorator function
def outerFn(fn):
    # 👉 Without "wraps", the returned wrapper loses the metadata (attributes) of the original function, like fn.__name__ and fn.__doc__.
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@outerFn
def greetMe(firstName, lastName=""):
    print(f"Hello {firstName} {lastName}")
    return "King"


print(greetMe("Python"))

# <---------------------------------> 🟡 DECORATOR WITH ARGUMENTS <--------------------------------->


# 🟡 Passing arguments from decorator need one extra inner function for receiving the actual "callback function"
def repeat(times):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for i in range(times):
                fn(*args, i, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def sayHello(name, time=0):
    print(f"{time} -- Hello {name}")


sayHello("Python")


# <---------------------------------> 🟡 DECORATOR WITH CLASS <--------------------------------->


class CountCalls:
    def __init__(self, fn: Callable[[str, int], None]) -> None:
        self.fn = fn
        self.count = 0

    def __call__(self, *args, **kwds) -> None:
        self.count += 1
        print(f"Call number {self.count}")
        return self.fn(*args, **kwds)


@CountCalls
def greetPython(name: str, age: int):
    print(f"Your name is {name}, and age is {age} right???")


greetPython("John", 14)
greetPython("Charlie", 10)
greetPython("Victor", 12)

# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(args[0], kwargs) # kwargs is a dictionary and args is a tuple --> if we pass a dict it goes on kwargs and if we pass only a value it goes on args
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet(message):
#     print(message)
#
# greet("Hello")


# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# print(add(3, 4))


# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before calling the function")
#         func(*args, **kwargs)
#         print("After calling the function")
#     return wrapper
#
# @log_decorator
# def greet(name):
#     print(f"Hello, {name}")
#
# greet("John")
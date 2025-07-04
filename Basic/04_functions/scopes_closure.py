# def maths(num):
#     def sum(num2):
#         return num + num2
#     return sum
#
# def maths2(num):
#     def sum():
#         return num + 10
#     return sum()
#
# print(maths(5)(55))
# print(maths2(10))


# def example(a, b=2):
#     c = a + b
#     def say_name(name = "Abdur Rab Khan"):
#         print(f"Hello {name}!",c)
#
#     return say_name
# #
# # print(example.__code__.co_varnames)
# # print(example.__defaults__)
# print(example.__closure__)


# Decorators in Python

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(name=kwargs["name"].lower())
#         return result
#     return wrapper
#
# @decorator
# def say_hello(*args,**kwargs):
#     print(f"Hello {kwargs["name"]}!!! ")
#
# print(say_hello.__name__)
# say_hello(name="Abdur Rab Khan")


# Method 2

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(kwargs)
        func("Babu")

    return wrapper


@decorator
def say_hello(name="Abdur Rab Khan"):
    print(f"Hello {name}!!!")

# say_hello = decorator(say_hello) --> say_hello() function is == to these thing.

say_hello(name="Lala Bhai")
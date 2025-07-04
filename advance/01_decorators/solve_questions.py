# Greeting decorator what call Hello! after calling the function and call Good Bye!! After the func called
import datetime
import time


# def greet(func):
#     def wrapper(*args,**kwargs):
#         print("Hello!!")
#         func()
#         print("GoodBye!!")
#
#     return wrapper
#
#
# @greet
# def say_hello(name="User"):
#     print(f"{name} you are so amazing")
#
# say_hello(name="Abdur Rab Khan")

# Problem 2: Timing Decorator

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"Function '{func.__name__}' took {end - start:.2f} seconds to run.")
#
#         return result
#
#     return wrapper
#
# @timer
# def looping():
#     time.sleep(2)
#     return "Stopped"
#
# print(looping())

# Problem 3: Argument-Passing Decorator

# def repeat(n):
#     def n_time_repeater(fun):
#         def wrapper():
#             for i in range(0, n):
#                 fun()
#
#         return wrapper
#
#     return n_time_repeater
#
# @repeat(n=3)
# def say_hello():
#     print("Hello")
#
# say_hello()

# Problem 4: Debugging Decorator

# def debug(func):
#     def wrapper(*args,**kwargs):
#         print(f"Calling function: {func.__name__}")
#         print(f"Arguments: {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Return value: {result}")
#         return result
#
#     return wrapper
#
# @debug
# def add(n,n2):
#     return n + n2
#
#
# add(2,2)

# Problem 5: Caching Decorator

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"Function '{func.__name__}' took {end - start:.2f} seconds to run.")
#
#         return result
#
#     return wrapper
#
# def cache(func):
#     cached_results = {}
#
#     def wrapper(*args,**kwargs):
#         num, = args
#         if cached_results.get(num):
#             return cached_results[num]
#
#         result = func(*args)
#         cached_results[num] = result
#         return result
#
#     return wrapper
#
# @cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(10))
# print(fibonacci(10))


# Problem 6: Access Control Decorator

# def access_control(func):
#     def wrapper(*args,**kwargs):
#         if kwargs["admin"]:
#             result = func(*args,**kwargs)
#             return  result
#         else:
#             print("Access Denied")
#
#     return wrapper
#
# @access_control
# def logging(*args,**kwargs):
#     time.sleep(1)
#     print("Logging successfully")
#
# logging(admin=True)
# logging(admin=False)

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} is called {start - end:.2f} take times")

    return wrapper

def logger(func):
    def wrapper(*args,**kwargs):
        print(f"func is started at {datetime.datetime.now().timestamp()}")
        result = func(*args,**kwargs)
        return result

    return wrapper

def repeat(n = 1):
    def decorators(func):
        def wrapper(*args,**kwargs):
            for i in range(0,n):
                print(f"hellow {n}")
                result = func(*args, **kwargs)

                return result
        return wrapper

    return decorators

@repeat(4)
@logger
@timer
def looping():
    time.sleep(2)

looping()
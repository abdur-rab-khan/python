from math import pi

# 1: Calculate square of the number

# def square_num(num):
#     return num ** 2
#
# print(f"The square of {5} is {square_num(5)}")

# Calculate the sum of two numbers
#
# 2: def calculate_sum_of_num(num1,num2):
#     return num1 + num2
#
# sum = calculate_sum_of_num(5,5)
# print(f"Result is: {sum}")

# 3. Polymorphism in Functions

# def multi_value(item1,item2):
#     return item1 * item2
#
# print(multi_value("Hello ",2))
# print(multi_value(2,2))

# 4 Function Returning Multiple Values

# def find_area_circum(radius):
#     area = pi * (radius ** 2)
#     circum = 2 * pi * radius
#     return area,circum
#
# area,circum = find_area_circum(5)
#
# print(f"Area of a circle is {area}")
# print(f"Circum of a circle is {circum}")

# 5. Default Parameter Value

# def greet_me(name = "Unknown"):
#     print(f"Assalam Walaikum {name}")
#
# greet_me("Abdur Rab Khan")
# greet_me()


# 6. Lambda Function
# cube = lambda x = 4: x**3
# new_cum = cube(10)
#
# print(cube())

# 7. Function with *args
#
# def sum_of_all(*args):
#     return sum(args)
#
# print(sum_of_all(1,2,3,4,5))


# 7. Function with **kwargs

# def print_kwargs(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# print_kwargs(name="shaktiman", power="lazer")

# def print_something(*args,**kwargs):
#     print(args,kwargs)
#
# list_details = {
#     "name":"Abdur Rab Khan",
#     "age":"21"
# }
#
# print_something(1,2,3,4,5,**list_details)
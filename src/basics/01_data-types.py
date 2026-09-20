from typing import List
from copy import deepcopy

# 1. Number Data Type
x = 20
y = 50

print("Multiplication of ", x, " and ", y, " is: " ,x * y)

# ** can be use to directly find the power of any number
print("Square of 4 is: ",4 ** 2)

# ❌ It's not possible in python, like in js using var
# print(z)
# z = 90

# 👉 String repeatation, "50" will gona repeat two times, it's won't automatically convert into number like in js.
string_num = "50"
print(string_num * 2) # 5050
print(int(string_num) * 2) # 100, explicit type casting "int" convert "50" into number 50
# float -> converts into floating point number

# 👉 Getting a type of any variable
print(type(string_num)) # <class str>
print(type(string_num) == str) # true

# Converting string char into ascii
character = 'a'
print("ASCII of a is: ", ord(character))

# <------------------------------------------------------> END <------------------------------------------------------>

# 2. String Data Type

# 👉 It's possible to make string using both '' (single quote) and "" (duble quote)
singleStr = 'Hello Python'
doubleStr = "Hello String"

print(singleStr + doubleStr) # String concatination

# "\" preceed to write escape like "\t (for tabs space)", "\n (for new line)", "("\"Python\", is good") -> Quote the string"
str1 = "C:\t Hello \"Python\", how are you!"
print(str1)

str2 = r"C:\home\name\t\x" # Since "\" used to write escape but using "r" we can say python to ignore "escape" just thing as raw string
print(str2) # C:\home\name\t\x

# * and + is used for repeating and concatinating the string
greet = "Hello "
name = "Python"
print(greet * 3 + name)


# 👉 Indexing, used to obtain particular element using the index number.
print(name[0]) # P

# 👉 Slicing, used to sequence of character via start and end index (name[start:end]).
"""
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""
print(name[0:2]) # Py
print(name[2:4]) # th
print(name[:2]) # "Py", We can skip start index, and python will assume 0
print(name[2:]) # "thon", We can also skip end index, and python will assume last index
print(name[-1]) # "n", last index
print(name[-2]) # o, second last index

# 👉 len function used to used the size of name
print("Size of name is: ", len(name))

print("123".isalnum())
print("abc".isalpha())


# <------------------------------------------------------> END <------------------------------------------------------>

# 3. List (Array) Data Type

squares: List[int] = [2, 4, 8, 16, 32]
cubes: List[int] = [1, 8, 27, 65, 25]

# 🟡 Indexing, Slicing, Contatication (+), Repeatition (*) is also allowed with list as well
print("Squares: ", squares)

print(squares[0]) # 2
print(squares[1: 3]) # [4, 8]
print(squares[1:]) # [4, 8, 16, 32]

# 👉 Concatinating two lists
print(squares + cubes) # [2, 4, 8, 16, 32, 1, 8, 27, 65, 25]

# 👉 Make single list by repeating the squares list two times
print(squares * 2) # [2, 4, 8, 16, 32, 2, 4, 8, 16, 32]

# 🟡 Common list methods
squares.append(2 ** 6) # Used to insert 2 ** 6 = 64 into the list

# 👉 Used to extend the current list from an iterable like (list, set, tuple, dict (keys))
squares.extend((11, 22, 33))
squares.extend({1000, 2000, 3000})
print(squares)

squares.pop() # Removes the index value, default is last index, ❌ Raise "IndexError" execption if not found
squares.remove(3000) # Removes the first occurence of a value, ❌ Raise "ValueError" exception if not found
squares.sort(
    reverse=False # Default is smaller to large, but using reverse "True" we can do large to smaller
) # Used to sort

squares_string = " - ".join(str(num) for num in squares)
print(squares_string) # 2 - 4 - 8 - 11 - 16 - 22 - 32 - 33 - 64 - 1000

# 👉 Shallow copy and Deep Copy
sqr_copy = squares.copy() # It's a shallow copy
sqr_deepcopy = deepcopy(squares) # It's a deepcopy

# 🟡 List Comprehensions, use to create new list where each element is the result of some operations of another list of iterable (list, set, tuple and dict)
sqr = [num ** 2 for num in range(2, 11)] # Range function used to generate sequence of interger, range(start, end, step)
print("Square: ", sqr)

# 👉 It's similar to nested loop for each
# Goes from LEFT TO RIGHT
# Where for each element of num1 first it checks x != 3, it not than run num3
# Then again check x != y if true than only (x, y) will run
num1 = [1, 2, 3]
num2 = [2, 1, 4]
nested_list = [(x, y) for x in num1 if x != 3 for y in num2 if x != y] # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(nested_list)

# 👉 Nested matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(len(matrix))])

for i, value in enumerate(["Hello", "World", "Python"]):
    print(f"Index: {i}, value: {value}")

# <------------------------------------------------------> END <------------------------------------------------------>

# 4. Dict is a hashmap data structure in python

# 👉 It's a key value pair data structure, key can be any immutable data type like (number, string and tuple)
my_dict = {
    "name": "Python",
    "age": 35,
    "released_at": {
       "date": 21,
       "month": "February",
       "year": 1991
    },
    ("key1", "key2", "key3"): "Tuple type",
}

print(my_dict.keys())
print(my_dict.values())

print("Value of name is: ", my_dict.get("name"))
print("Value of name is: ", my_dict[("key1", "key2", "key3")])

# items() returns the set-like data structure
for key, value in my_dict.items():
    print(f"Key is: {key}, value is: {value}")

my_dict.update({"name": "Python3"})

# <------------------------------------------------------> END <------------------------------------------------------>

# 5. Set in python is unordered collection of elements with no duplicates and math operations like "union", "intersection", "difference" etc
bucket = {'apple', 'orange', 'apple', 'pears'}

print("Is apple is there: ", "apple" in bucket) # o(1) for access

# <------------------------------------------------------> END <------------------------------------------------------>

# 6. Tuple Data Type, it's non-mutable data structure, that's why it's good for using tuple as a key in dict

tup1 = "a", "b", "c", "d" # First way using "," seperated to create tuple
print(tup1)

tup2 = ("a", "b", "c", "d") # Using parentheses
print(tup2)

# tup1[0] = "55", you can't do that.

# 👉 Packing an unpacking elements
a = 55
b = 66
c = 88
d = [1, 2, 3, 4]

abc_pack = a, b, c, d
print(abc_pack)

# 👉 Reassigning 'a' doesn't change the tuple because integers are immutable (a now points to a new number).
# 👉 Modifying 'd' changes the tuple because lists are mutable, and the tuple just holds a reference to that list.
a = 44
d[0] = 88
print(abc_pack)


# 👉 Unpacking
a1, b2, c2, d2 = abc_pack
print(a1, " ", b2, " ", c2, " ",d2)

# <------------------------------------------------------> END <------------------------------------------------------>

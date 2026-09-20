# Looping

# Looping through a list
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# Output: apple, banana, cherry

# Looping through a string
for letter in 'banana':
    print(letter)

# Output:  b, a, n, a, n, a


# Looping through a range of numbers

for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4

# Looping through a range with a step

for i in range(0, 10, 2):
    print(i)

# Output: 0, 2, 4, 6, 8

# Looping through a dictionary

person = {'name': 'John', 'age': 30, 'city': 'New York'}

for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: John
# age: 30
# city: New York

# Looping through a set

fruits_set = {'apple', 'banana', 'cherry'}

for fruit in fruits_set:
    print(fruit)

# Output: apple, banana, cherry (order may vary since sets are unordered)

# Looping with an index using enumerate

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# Looping with a while loop

count = 0
while count < 5:
    print(count)
    count += 1

# Output: 0, 1, 2, 3, 4

# Looping with a break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Output: 0, 1, 2, 3, 4

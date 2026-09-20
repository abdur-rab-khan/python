# len(list)
lst = [1, 2, 3]
print(len(lst))  # 3

# append()
lst = [1, 2]
lst.append(3)  # [1, 2, 3]

# extend()
lst = [1, 2]
lst.extend([3, 4])  # [1, 2, 3, 4]

# insert()
lst = [1, 3]
lst.insert(1, 2)  # [1, 2, 3]

# remove()
lst = [1, 2, 3, 2]
lst.remove(2)  # [1, 3, 2] (removes first 2)

# pop()
lst = [1, 2, 3]
lst.pop()  # 3, lst becomes [1, 2]
lst.pop(0)  # 1, lst becomes [2]

# clear()
lst = [1, 2, 3]
lst.clear()  # []

# copy()
original = [1, 2, 3]
copied = original.copy()  # [1, 2, 3]

# count()
lst = [1, 2, 2, 3]
print(lst.count(2))  # 2

# index()
lst = [10, 20, 30]
print(lst.index(20))  # 1

# reverse()
lst = [1, 2, 3]
lst.reverse()  # [3, 2, 1]

# sort()
lst = [3, 1, 2]
lst.sort()  # [1, 2, 3]
lst.sort(reverse=True)  # [3, 2, 1]

# slicing
lst = [1, 2, 3, 4, 5]
print(lst[1:3])  # [2, 3]
print(lst[:2])   # [1, 2]
print(lst[2:])   # [3, 4, 5]
print(lst[-2:])  # [4, 5]

# list comprehension
squared = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# enumerate
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(index, value)  # 0 a, 1 b, 2 c

# range to list
print(list(range(5)))  # [0, 1, 2, 3, 4]

# nested lists
nested = [[1, 2], [3, 4]]
print(nested[0])  # [1, 2]
print(nested[1][0])  # 3

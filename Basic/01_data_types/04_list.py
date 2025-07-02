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

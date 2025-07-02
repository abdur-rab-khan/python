s = {1, 2}
s.add(3)  # s becomes {1, 2, 3}

# clear()
s = {1, 2, 3}
s.clear()  # s becomes set()

# copy()
s = {1, 2, 3}
new_s = s.copy()  # new_s is {1, 2, 3}

# difference()
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))  # {1, 3}

# difference_update()
a = {1, 2, 3}
b = {2, 4}
a.difference_update(b)  # a becomes {1, 3}

# discard()
s = {1, 2}
s.discard(2)  # s becomes {1}
s.discard(5)  # no error, s stays {1}

# intersection()
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))  # {2, 3}

# intersection_update()
a = {1, 2, 3}
b = {2, 4}
a.intersection_update(b)  # a becomes {2}

# isdisjoint()
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True

# issubset()
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True

# issuperset()
a = {1, 2, 3}
b = {2}
print(a.issuperset(b))  # True

# pop()
s = {1, 2, 3}
s.pop()  # removes a random element

# remove()
s = {1, 2}
s.remove(2)  # s becomes {1}
# s.remove(5)  # would raise KeyError

# symmetric_difference()
a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))  # {1, 2, 4}

# symmetric_difference_update()
a = {1, 2, 3}
b = {2, 4}
a.symmetric_difference_update(b)  # a becomes {1, 3, 4}

# union()
a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

# update()
a = {1}
b = {2, 3}
a.update(b)  # a becomes {1, 2, 3}

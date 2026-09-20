# get()
person = {"name": "Alice", "age": 30}
print(person.get("name"))         # Alice
print(person.get("gender", "N/A"))  # N/A

# update()
# {'name': 'Alice', 'age': 31, 'city': 'New York'}
person.update({"age": 31, "city": "New York"})

# items()
# dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')])
print(person.items())

# keys()
print(person.keys())  # dict_keys(['name', 'age', 'city'])

# values()
print(person.values())  # dict_values(['Alice', 31, 'New York'])

# copy()
copy_person = person.copy()  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# pop()
# 31, person becomes {'name': 'Alice', 'city': 'New York'}
age = person.pop("age")

# popitem()
last_item = person.popitem()  # removes ('city', 'New York')

# setdefault()
person.setdefault("gender", "Female")  # Adds 'gender': 'Female' if not present

# clear()
person.clear()  # {}

# fromkeys()
# {'id': 'unknown', 'role': 'unknown'}
defaults = dict.fromkeys(["id", "role"], "unknown")

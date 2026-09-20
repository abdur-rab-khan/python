a = 55
b = 66

# 🟡 Basic if elif else Statement
if a == b:
    print(f"{a} and b is same")
elif a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is smaller than {b}")


# 👉 We can use "and", "or" and "not" at the place of "&&" "||" and "!"
is_true = True
if is_true and a < b:
    print("Yes it's matched the condition")

if not is_true or a != b:
    print(f"{a} {b} is not equal or is_true is false")

# 🟡 Match case statement
# if (day := input("Enter your day: ")) != "" and day.isdigit():
#     match int(day):
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case _:
#             print("Not implemented yet")
# else:
#     print("Invalid input")


# 🟡 Looping in Python

# 👉 It returns sequence of number from start to end with steps, reversed just reverse the number
for i in reversed(range(1, 11)):
    print(i, end=" ")
print(end="\n\n")

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print(f'Question is: "{q}" and answer is: "{a}"')


i = 5
while i >= 0:
    print(i, end=" ")
    i -= 1
print(end="\n\n")

# 👉 Loop in list, with and without indexing
for val in ["apple", "banana", "mango"]:
    print(val, end=" ")

print(end="\n\n")

for idx, val in enumerate(["apple", "banana", "mango"]):
    print(f"Index: {idx}, value: {val}")


# 👉 Loop in dict
dict1 = {"name": "Python", "age": 35}

# 👉 Just iterate on the dict key
for key in dict1:
    print(f"Key is: {key}")

# 👉 Iterating through key, value at the same time
for key, val in dict1.items():
    print(f"Key {key}, Value {val}")

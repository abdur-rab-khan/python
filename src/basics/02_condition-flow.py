a = 55
b = 66

# 🟡 Basic if elif else Statement
if a == b:
    print(f"{a} and b is same")
elif a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is smaller than {b}")


# 👉 We can use "and", "or" at the place of &&, ||
is_true = True
if is_true and a < b:
    print("Yes it's matched the condition")

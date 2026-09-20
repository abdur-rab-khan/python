# 👉 Function without any args, using "def" keyboard, and optionally first line can be use for docs
def greet() -> None:
    """Simple greet function"""
    print("Hello Python")


greet()


# 👉 Function with args with types
def greet(name: str, fav_lang="C++") -> None:
    print(f"Hello {name}, your favorite language is: {fav_lang}")


greet("Charlie", "Python")
greet(
    fav_lang="C++", name="John"
)  # You can pass like that as well, not here we don't need to worry about position of args


# 👉 Closure in Python Function
def power(n: int):
    def cal(num: int):
        return num**n

    return cal


squareFn = power(2)
print("Power of 2^2: ", squareFn(2))
print("Power of 2^3: ", squareFn(3))
print("Power of 2^4: ", squareFn(4))

"""
🟡 All the variables define in the function store in the "new Symbol table", created once function is call.
🟡 Similar to JS, If you try to use a variable first it look at the:
    1. "Local Symbol Table" -> if not found then
    2. "Local Symbole of enclosing fun" (If fn is closure) -> if not found then
    3. "Global Symbol Table" -> if not found then
    4. At the end "Table of built-in names"
"""
name = "Python"


def noNameFn():
    # 👉 Since we don't have any keyword for defining a variable, it's looks same when you define and redeclaring a variable.
    # 👉 In a case where you want to update the global variable you must tell i'm gonna use global variable don't define this in to the local scope just redeclare the global variable using "global" keyword.
    # 👉 In closure function if you want to redeclare parent function variable you can use "nonlocal" keyword
    # global name
    name = "C++"
    print(name)


noNameFn()
print(name)


# 🟡 *args and **kwargs
# 👉 args: Recieves Tuples of Values
# 👉 **kwargs Recieves dict of values
def noNameFn(name, *args, **kwargs):
    print(f"Name is: {name}")
    print(f"Arguments are: {args}")
    print(f"Kwargs are: {kwargs}")


# Similar to JS "...", "**" in Python use to unpack dict
noNameFn("John", 2, 3, 4, "Python", "C++", **{"fav_lang": "Python", "age": 35})
noNameFn("John", 2, 3, 4, "Python", "C++", fav_lang="C++", age=35)

list1 = [1, 2, 3]
list2 = [11, 22, 33, *list1]
print(list2)

dict1 = {"fav_lang": "Python", "age": 25}
dict2 = {"age": 35}
print({**dict1, **dict2})

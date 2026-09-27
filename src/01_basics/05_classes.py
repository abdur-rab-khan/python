# 🟡 Classes are used to bundle data and methods that operate on the data together.
# 🟡 Python classes and instances have namespaces (dict) that map names to objects. For a normal object, attributes assigned using "self." are stored in the instance namespace, while class attributes are stored in the class namespace.
# 🟡 We can access the instance namespace via "object.__dict__" and the class namespace via "Class.__dict__".

# 👉 More better way to say that, that have two instance:
#       1. Class Object: Things that belongs to class it self, like "Class.__doc__", "Class.skills".
#       2. Instance Object: Things that belongs to a particular instance of class, like "object.instance_skills"

# ⭕ Access Modifier in Python Classes:
#       1. "_variableName"          (Protected)
#       2. "__variableName"         (Private)


from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override


class Player:
    # 👉 There are only one skills list stored on the classes, every object just point to this one.
    # 👉 It's good choice to keep everything in current instance level, like we did with "self.instance_skills"
    skills = ["kick", "jump-attack"]

    # 👉 "__init__" function call once object is created
    def __init__(self):
        # It directly goes into instance "namespace", so everything we object is create a namespace (dict) attached with it,
        # Anything we put using "self." directly goes into that namespace (dict)
        self.instance_skills = ["fire", "roll up"]


player1 = Player()
print("Player class skills", player1.skills)
print("Player 2 instance skills: ", player1.instance_skills)

player1.skills.append("karate")

player2 = Player()
print("Player class skills", player2.skills)
print("Player 2 instance skills: ", player2.instance_skills)

print(end="\n\n")

# <-------------------------------------> END <------------------------------------->


# 🟡 OOPs in Python, like in other programing languages python also support inheritance
# 🟡 Like in python scope first look at local scope, than move on. In class as well first look at current class move to there decedent class.
class BaseClass:
    def __init__(self, name: str) -> None:
        self._name = name

    def greeting(self):
        print("Hello sir")


class DerivedClass(BaseClass):
    # 👉 Overriding: There isn't any-special thing to override the base class function, by default every function are "virtual"
    def greeting(self):
        print(f"Hello {self._name} good morning")


print(end="\n")

# <-------------> END <------------->

d = DerivedClass(name="Python")
d.greeting()


# 🟢 Multiple Inheritance
class Base1:
    def sayHello(self):
        print("Hello boss")


class Base2:
    def greeting(self):
        print("Hello good morning boss")


class Derived(Base1, Base2):
    pass


dd = Derived()
# Anything we call they first look at derived class then recursively move to it's base classes
print(dd.greeting())
print(dd.sayHello())


print(end="\n\n")

# <-------------------------------------> END <------------------------------------->


# 🟡 Special decorators for Python Classes


# 1. @dataclass --> Similar to C/C++ struct use to store data items
@dataclass
class Employee:
    name: str
    dept: str
    salary: int


print(Employee(name="Python", dept="IT", salary=0))


# 2. @staticmethod --> Similar to static in C++, it does not receives "self (current object namespace)" and "cls (class namespace)"
class Math:
    @staticmethod
    def add(a, b):
        return a + b


m = Math()
print(m.add(2, 2))


# 3. @classmethod --> It's just only receive "cls (class namespace)", now we can do anything with class
class User:
    def __init__(self, name: str, age: int):
        self.name = name.strip()
        self.age = age

    def getDetails(self):
        return f"Name is: {self.name}\nAge is: {self.age}"

    @classmethod
    def from_string(cls, data: str):
        name, age = data.split(",")
        return cls(name, int(age))


print(User.from_string("Python,35").getDetails(), end="\n\n")

# <-------------------------------------> END <------------------------------------->

# 🟡 Getter/Setter in Python Classes


# <-------------------------------------> END <------------------------------------->


# 🟡 Abstract (Interfaces) function in python
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    @override
    def speak(self):
        print("Bark Bark")


dog = Dog()
dog.speak()

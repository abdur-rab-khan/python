# 🟡 Classes are used to bundle data and methods that operate on the data together.
# 🟡 Python classes and instances have namespaces that map names to objects. For a normal object, attributes assigned using "self." are stored in the instance namespace, while class attributes are stored in the class namespace.
# 🟡 We can access the instance namespace via "object.__dict__" and the class namespace via "Class.__dict__".


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

# <-------------------------------------> END <------------------------------------->

# 🟡 OOPS concept in Python Classes


# <-------------------------------------> END <------------------------------------->

# 🟡 Special decorators for Python Classes

# <-------------------------------------> END <------------------------------------->

# 🟡 Getter/Setter in Python Classes


# <-------------------------------------> END <------------------------------------->

# 🟡 Context Manager in Python

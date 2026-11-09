# Declaring String using C-Style.

# Declaring String using std::string class.

# Strings are immutable in C++

# name[0] = 'B'; // ❌ You can't manipulate the string literal, It is immutable

# ✔️ It is possible to manipulate std::string.

def demo_string():
    name = "Abdur Rab Khan"
    print("Python string:", name)
    first_name = "Abdul"
    first_name = first_name[:-1] + "r"
    print(first_name)

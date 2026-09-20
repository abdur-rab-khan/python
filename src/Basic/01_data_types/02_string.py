s = "hello world"

# capitalize
print(s.capitalize())  # Hello world

# casefold
print("HELLO".casefold())  # hello

# center
print("hi".center(10, '-'))  # ----hi----

# count
print("banana".count("a"))  # 3

# encode
print("hello".encode())  # b'hello'

# endswith
print("test.py".endswith(".py"))  # True

# expandtabs
print("a\tb\tc".expandtabs(4))  # a   b   c

# find
print("hello".find("e"))  # 1

# format
print("Hello, {}!".format("Alice"))  # Hello, Alice!

# format_map
print("Age: {age}".format_map({"age": 30}))  # Age: 30

# index
print("hello".index("e"))  # 1

# isalnum
print("abc123".isalnum())  # True

# isalpha
print("abc".isalpha())  # True

# isascii
print("abc".isascii())  # True

# isdecimal
print("123".isdecimal())  # True

# isdigit
print("123".isdigit())  # True

# isidentifier
print("var_1".isidentifier())  # True

# islower
print("hello".islower())  # True

# isnumeric
print("123".isnumeric())  # True

# isprintable
print("Hello!".isprintable())  # True

# isspace
print("   ".isspace())  # True

# istitle
print("Hello World".istitle())  # True

# isupper
print("HELLO".isupper())  # True

# join
print(",".join(["a", "b", "c"]))  # a,b,c

# ljust
print("hi".ljust(5, "."))  # hi...

# lower
print("HELLO".lower())  # hello

# lstrip
print("   test".lstrip())  # test

# maketrans & translate
trans = str.maketrans("abc", "123")
print("abc".translate(trans))  # 123

# partition
print("key:value".partition(":"))  # ('key', ':', 'value')

# removeprefix
print("TestHook".removeprefix("Test"))  # Hook

# removesuffix
print("misc.txt".removesuffix(".txt"))  # misc

# replace
print("one one one".replace("one", "two"))  # two two two

# rfind
print("banana".rfind("a"))  # 5

# rindex
print("banana".rindex("a"))  # 5

# rjust
print("hi".rjust(5, "."))  # ...hi

# rpartition
print("key:value".rpartition(":"))  # ('key', ':', 'value')

# rsplit
print("a,b,c".rsplit(",", 1))  # ['a,b', 'c']

# rstrip
print("test   ".rstrip())  # test

# split
print("a,b,c".split(","))  # ['a', 'b', 'c']

# splitlines
print("a\nb\nc".splitlines())  # ['a', 'b', 'c']

# startswith
print("hello.py".startswith("hello"))  # True

# strip
print("  test  ".strip())  # test

# swapcase
print("Hello".swapcase())  # hELLO

# title
print("hello world".title())  # Hello World

# upper
print("hello".upper())  # HELLO

# zfill
print("42".zfill(5))  # 00042

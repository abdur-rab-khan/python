# from by import By --> For Same Level import, we can import it directly from the package
# If hello function call anywhere other than may cause error because of when they try to find by.py file it will not be found because it is not in the same directory as hello.py so we have to do like below ⬇️
from .by import By


def Hello():
    By()
    print("Hello, World!")


# By() --> Same Level

# from same_level.by import By --> We add import already on the __init__.py file of the same_level package so we can import it directly from the package
from same_level import By, Hello
from dir_level.lib import call_name, say_name, call_utils

By()
Hello()

call_name()
call_utils()

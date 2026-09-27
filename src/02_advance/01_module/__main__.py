"""
🟡 What is "module" in Python:
    1. "module" is just a ".py" file, that have there own namespace (global scope) and to get name for the namespace we can just "import" statement.
    2. To directly import name from module, we can do like this "from module import name/another-module", "import module" then "module.name".
    3. "dir()" use to find-out all the "variables", "functions", "modules" of current file.
    4. Once we import any module in the current file first it look at "built-in modules", files in "sys.path" directories.

🟡 What is "packages" in Python:
    1. "packages" is a way to structure different modules into a packages like a packages can have "modules" or "sub-packages".
    2. In Python "__init__.py" is required to make any directory into package.
    3. Usually "__init__.py" are import but we can have a special variable "__all__ = ["modules", "sub-package"]" only listed "packages" and "sub-packages" will include if we import like this "from package import *".
    4. To run a package we usually use "python -m package:filename", but if filename is "__main__.py" we actually don't need to manually add ":filename".
"""

from routes import a, b

a.greetFn()
b.greetFn()


def main():
    print("🎉 Running module.py successfully")


if __name__ == "__main__":
    main()

def logging_protect(path=None):
    if not path:
        raise ValueError("Please provide a correct path")

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check if username and password are provided
            if not all(args[1:]):  # Skip 'self' in args
                raise ValueError("Username and password are required")

            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


class App:
    def __init__(self):
        self._username = "abdurrabkhan222"  # Use protected attributes
        self._password = 12345  # Use protected attributes

    @logging_protect(path="auth.login")
    def logging(self, username, password):
        # Convert password to integer for validation
        try:
            password = int(password)
        except ValueError:
            raise ValueError("Password must be an integer")

        if username != self._username or password != self._password:
            raise ValueError("Invalid username or password")

        return "Logging Successful"

    @property
    def username(self):
        raise AttributeError("You can't get the username")

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Username must be a non-empty string")
        self._username = value  # Assign to protected attribute

    @property
    def password(self):
        raise AttributeError("You can't get the password")

    @password.setter
    def password(self, value):
        if not isinstance(value, int) or value <= 4:
            raise ValueError("Password must be an integer greater than 4")
        self._password = value  # Assign to protected attribute


# Create an instance of App
app = App()

# Simulate a login loop
while True:
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        result = app.logging(username, password)
        print(result)
        break
    except ValueError as error:
        print(error)
    except AttributeError as error:
        print(error)
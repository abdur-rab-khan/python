# Classes and Objects in Python

- [Classes and Objects in Python](#classes-and-objects-in-python)
  - [Terms in Classes](#terms-in-classes)
  - [Advance methods in python](#advance-methods-in-python)
    - [1. **Inheritance in Python**](#1-inheritance-in-python)
    - [2. **Encapsulation in Python**](#2-encapsulation-in-python)
    - [**Access Modifiers in Python**](#access-modifiers-in-python)
    - [**Polymorphism in Python**](#polymorphism-in-python)
    - [**Abstraction in Python**](#abstraction-in-python)
    - [**Special Methods (Magic Methods)**](#special-methods-magic-methods)
    - [Getter and Setters](#getter-and-setters)
      - [**Getter and Setter Using `@property`**](#getter-and-setter-usingproperty)
      - [**Read-Only Attributes**](#read-only-attributes)
      - [**Write-Only Attributes**](#write-only-attributes)
      - [**Computed Attributes**](#computed-attributes)
      - [**Key Points**](#key-points)
    - [**Summary of Key Concepts**](#summary-of-key-concepts)

> A **class** is a blueprint or template for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have. \
> An **object** is an instance of a class. When a class is defined, no memory is allocated until an object is created from that class.

## Terms in Classes

1. **Class Definition**:
    - The `Dog` class is defined with a class attribute (`species`) and instance attributes (`name` and `age`).
    - The `__init__` method is the constructor, which is called when an object is created. It initializes the instance attributes.
    - The `bark` and `get_age` methods are instance methods that operate on the object's data.
2. **Object Creation**:
    - `dog1` and `dog2` are objects (instances) of the `Dog` class.
    - Each object has its own `name` and `age` attributes.
3. **Accessing Attributes and Methods**:
    - Use dot notation (e.g., `dog1.name`) to access attributes and call methods.

## Advance methods in python

### 1. **Inheritance in Python**

> Inheritance is a mechanism that allows a class (called a **child class** or **subclass**) to inherit attributes and methods from another class (called a **parent class** or **superclass**). This promotes code reuse and modularity.

- **Example of Inheritance**

    ```python
    # Parent class
    class Animal:
        def __init__(self, name):
            self.name = name
    
        def speak(self):
            return f"{self.name} makes a sound."# Child class (inherits from Animal)
    class Cat(Animal):
        def __init__(self, name, color):
            # Call the parent class constructor
            super().__init__(name)
            self.color = color
    
        # Override the speak method
        def speak(self):
            return f"{self.name} says meow!"# New method specific to Cat class
        def describe(self):
            return f"{self.name} is a {self.color} cat."# Create objects
    animal = Animal("Generic Animal")
    cat = Cat("Whiskers", "black")
    
    # Access methods
    print(animal.speak())  # Output: Generic Animal makes a sound.
    print(cat.speak())     # Output: Whiskers says meow!
    print(cat.describe())  # Output: Whiskers is a black cat.
    ```

  - **Explanation of Inheritance**
    1. **Parent Class (`Animal`)**:
        - Defines a `speak` method and an `__init__` method.
    2. **Child Class (`Cat`)**:
        - Inherits from `Animal` using `class Cat(Animal)`.
        - Calls the parent class constructor using `super().__init__(name)`.
        - Overrides the `speak` method to provide a specific implementation for cats.
        - Adds a new method `describe` specific to the `Cat` class.
    3. **Polymorphism**:
        - The `speak` method behaves differently for `Animal` and `Cat` objects, demonstrating polymorphism.

### 2. **Encapsulation in Python**

> Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (a class). Encapsulation also involves restricting direct access to some of an object's components, which is achieved using **access modifiers**.

### **Access Modifiers in Python**

- Python uses naming conventions to indicate the level of access:

    1. **Public**: Attributes and methods are accessible from anywhere.
        - No special syntax. Example: `self.name`
    2. **Protected**: Attributes and methods are accessible within the class and its subclasses.
        - Indicated by a single underscore (`_`). Example: `self._name`
    3. **Private**: Attributes and methods are accessible only within the class.
        - Indicated by a double underscore (`__`). Example: `self.__name`

- **Example of Encapsulation**

    ```python
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner  # Public attribute
            self._balance = balance  # Protected attribute
            self.__pin = "1234"  # Private attribute
    
        # Public method to deposit money
        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
                print(f"Deposited {amount}. New balance: {self._balance}")
            else:
                print("Invalid deposit amount.")
    
        # Public method to withdraw money
        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew {amount}. New balance: {self._balance}")
            else:
                print("Invalid withdrawal amount.")
    
        # Public method to display balance
        def display_balance(self):
            print(f"Balance: {self._balance}")
    
        # Private method to validate PIN
        def __validate_pin(self, pin):
            return self.__pin == pin
    
        # Public method to access private method
        def check_pin(self, pin):
            if self.__validate_pin(pin):
                print("PIN is correct.")
            else:
                print("PIN is incorrect.")
    
    # Create an object
    account = BankAccount("Alice", 1000)
    
    # Access public attributes and methods
    print(account.owner)  # Output: Alice
    account.deposit(500)  # Output: Deposited 500. New balance: 1500
    account.withdraw(200)  # Output: Withdrew 200. New balance: 1300
    account.display_balance()  # Output: Balance: 1300
    
    # Access protected attribute (not recommended, but possible)
    print(account._balance)  # Output: 1300
    
    # Access private attribute (will raise an error)
    # print(account.__pin)  # AttributeError: 'BankAccount' object has no attribute '__pin'
    
    # Access private method via public method
    account.check_pin("1234")  # Output: PIN is correct.
    account.check_pin("0000")  # Output: PIN is incorrect.
    ```

- **Key Points on Encapsulation**

  - Encapsulation ensures that the internal representation of an object is hidden from the outside world.
  - Protected and private attributes/methods are not truly restricted in Python; they are more of a convention to indicate intended usage.
  - Use getter and setter methods to control access to attributes if needed.

### **Polymorphism in Python**

> Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables methods to behave differently based on the object that calls them.

- **Example of Polymorphism**

    ```python
    class Animal:
        def speak(self):
            return "Animal sound"
    
    class Dog(Animal):
        def speak(self):
            return "Woof!"
    
    class Cat(Animal):
        def speak(self):
            return "Meow!"
    
    # Polymorphism in action
    def make_animal_speak(animal):
        print(animal.speak())
    
    dog = Dog()
    cat = Cat()
    
    make_animal_speak(dog)  # Output: Woof!
    make_animal_speak(cat)  # Output: Meow!
    ```

### **Abstraction in Python**

> Abstraction is the concept of hiding complex implementation details and showing only the necessary features of an object. In Python, abstraction is achieved using **abstract classes** and **interfaces**.

- **Example of Abstraction**

    ```python
    from abc import ABC, abstractmethod
    
    # Abstract class
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
    
        @abstractmethod
        def perimeter(self):
            pass
    
    # Concrete class
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
    
        def area(self):
            return 3.14 * self.radius ** 2
    
        def perimeter(self):
            return 2 * 3.14 * self.radius
    
    # Create an object
    circle = Circle(5)
    print(circle.area())  # Output: 78.5
    print(circle.perimeter())  # Output: 31.4
    ```

### **Special Methods (Magic Methods)**

> Special methods in Python are predefined methods that start and end with double underscores (`__`). They allow you to define how objects of a class behave with built-in operations like addition, comparison, and string representation.

- **Common Special Methods**

    1. `__init__`: Constructor method, called when an object is created.
    2. `__str__`: Returns a string representation of the object (used by `print()`).
    3. `__repr__`: Returns an unambiguous string representation of the object (used for debugging).
    4. `__add__`: Defines behavior for the `+` operator.
    5. `__eq__`: Defines behavior for the `==` operator.

- **Example of Special Methods**

    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def __str__(self):
            return f"Point({self.x}, {self.y})"
    
        def __repr__(self):
            return f"Point(x={self.x}, y={self.y})"
    
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)
    
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
    
    # Create objects
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    
    # Use special methods
    print(p1)  # Output: Point(1, 2)
    print(repr(p1))  # Output: Point(x=1, y=2)
    
    p3 = p1 + p2
    print(p3)  # Output: Point(4, 6)
    
    print(p1 == p2)  # Output: False
    ```

### Getter and Setters

> **Getters** and **setters** are methods used to control access to the attributes of a class. They are particularly useful for enforcing validation or constraints when getting or setting the value of an attribute. In Python, you can implement getters and setters using the `@property` decorator and the `@<attribute>.setter` decorator.

- **Why Use Getters and Setters?**
    1. **Encapsulation**: Hide the internal representation of an attribute.
    2. **Validation**: Ensure that only valid data is assigned to an attribute.
    3. **Computed Attributes**: Dynamically compute the value of an attribute when accessed.
    4. **Read-Only or Write-Only Attributes**: Restrict access to certain attributes.

#### **Getter and Setter Using `@property`**

> In Python, the `@property` decorator is used to define a **getter** method, and the `@<attribute>.setter` decorator is used to define a **setter** method.

- **Example**

    ```python
    class Person:
        def __init__(self, name, age):
            self._name = name  # Protected attribute
            self._age = age    # Protected attribute
    
        # Getter for name
        @property
        def name(self):
            return self._name
    
        # Setter for name
        @name.setter
        def name(self, value):
            if isinstance(value, str) and len(value) > 0:
                self._name = value
            else:
                raise ValueError("Name must be a non-empty string.")
    
        # Getter for age
        @property
        def age(self):
            return self._age
    
        # Setter for age --> If you want to use Setter you have to declare gettin from age
        @age.setter
        def age(self, value):
            if isinstance(value, int) and value >= 0:
                self._age = value
            else:
                raise ValueError("Age must be a non-negative integer.")
    
    # Create an object
    person = Person("Alice", 25)
    
    # Access attributes using getters
    print(person.name)  # Output: Alice
    print(person.age)   # Output: 25
    
    # Modify attributes using setters
    person.name = "Bob"
    person.age = 30
    
    print(person.name)  # Output: Bob
    print(person.age)   # Output: 30
    
    # Try setting invalid values
    try:
        person.name = ""  # Empty string
    except ValueError as e:
        print(e)  # Output: Name must be a non-empty string.
    
    try:
        person.age = -5  # Negative age
    except ValueError as e:
        print(e)  # Output: Age must be a non-negative integer.
    ```

- **Explanation of the Code**

    1. **Protected Attributes**:
        - `_name` and `_age` are protected attributes (indicated by a single underscore `_`). They are not truly private but are intended to be accessed only through getters and setters.
    2. **Getter**:
        - The `@property` decorator is used to define a getter method. For example, the `name` method is a getter for the `_name` attribute.
    3. **Setter**:
        - The `@<attribute>.setter` decorator is used to define a setter method. For example, the `name` method is also a setter for the `_name` attribute.
    4. **Validation**:
        - The setter methods include validation logic to ensure that only valid values are assigned to the attributes.

#### **Read-Only Attributes**

> You can create read-only attributes by defining only a getter method and not providing a setter method.

- **Example**

    ```python
    class Circle:
        def __init__(self, radius):
            self._radius = radius
    
        # Getter for radius (read-only)
        @property
        def radius(self):
            return self._radius
    
    # Create an object
    circle = Circle(5)
    
    # Access the read-only attribute
    print(circle.radius)  # Output: 5
    
    # Try to modify the read-only attribute (will raise an error)
    try:
        circle.radius = 10  # AttributeError: can't set attribute
    except AttributeError as e:
        print(e)
    ```

#### **Write-Only Attributes**

> You can create write-only attributes by defining only a setter method and not providing a getter method.

- **Example**

    ```python
    class Secret:
        def __init__(self):
            self._secret_value = None
    
        # Setter for secret_value (write-only)
        @property
        def secret_value(self):
            raise AttributeError("Cannot read secret_value.")
    
        @secret_value.setter
        def secret_value(self, value):
            self._secret_value = value
    
    # Create an object
    secret = Secret()
    
    # Set the write-only attribute
    secret.secret_value = "Top Secret"
    
    # Try to access the write-only attribute (will raise an error)
    try:
        print(secret.secret_value)  # AttributeError: Cannot read secret_value.
    except AttributeError as e:
        print(e)
    ```

#### **Computed Attributes**

> Getters can also be used to compute the value of an attribute dynamically.

- **Example**

    ```python
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
    
        # Computed attribute for area
        @property
        def area(self):
            return self.width * self.height
    
    # Create an object
    rectangle = Rectangle(4, 5)
    
    # Access the computed attribute
    print(rectangle.area)  # Output: 20
    ```

#### **Key Points**

- Use `@property` to define a getter method.
- Use `@<attribute>.setter` to define a setter method.
- Getters and setters allow you to control access to attributes and enforce validation.
- You can create read-only or write-only attributes by omitting the setter or getter, respectively.
- Computed attributes can be implemented using getters.

### **Summary of Key Concepts**

1. **Encapsulation**: Bundling data and methods, restricting access using naming conventions.
2. **Polymorphism**: Allowing objects of different classes to be treated as objects of a common superclass.
3. **Abstraction**: Hiding complex implementation details and showing only necessary features.
4. **Special Methods**: Predefined methods to define object behavior with built-in operations.

Let me know if you need further clarification or examples!

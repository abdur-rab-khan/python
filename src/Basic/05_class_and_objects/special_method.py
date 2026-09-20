class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y}) Hello Sir!!"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Create objects
p1 = Point(1, 2)
p2 = Point(3, 4)


# Use Special Method
print(p1)

print(repr(p1))

p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
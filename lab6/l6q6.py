# Define a class Vector with attributes x and y. Overload the + operator to add
# two Vector objects. Implement the __add__() method and test it by adding
# two Vector instances.

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x} i + {self.y} j"

v1 = Vector(4, 5)
v2 = Vector(6, -1)

result = v1 + v2
print(result)
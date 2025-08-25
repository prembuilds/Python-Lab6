# Create a base class Shape with a method area(). Derive two classes
# Rectangle and Circle from Shape. Implement the area() method in both
# derived classes. Instantiate Rectangle and Circle, and demonstrate
# polymorphism by calling their area() methods.

class Shape:
    
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length * self.width)

    def __str__(self):
        return f"{self.area()} m^2"
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (3.1415 * self.radius ** 2)

    def __str__(self):
        return f"{self.area()} m^2"
    

s1 = Rectangle(4,5)
s2 = Circle(5)

print(s1)
print(s2)
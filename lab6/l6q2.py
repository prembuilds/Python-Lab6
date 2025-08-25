# Create a base class Animal with a method speak() that prints "Animal makes
# a sound". Derive a class Dog from Animal and override the speak() method
# to print "Dog barks". Instantiate the Dog class and call its speak() method.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print(f"{self.name} Barks")

ob1 = Dog("Charlie")
ob1.speak()
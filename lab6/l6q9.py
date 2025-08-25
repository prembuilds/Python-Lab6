# Define a class Person with attributes name and age. Define another class
# Address with attributes street, city, and zipcode. Create a Contact class that
# contains an instance of Person and Address. Implement methods to display
# the contact details. Create a Contact object and display its information.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Contact:
    def __init__(self, name, age, street, city, zipcode):
        self.person = Person(name, age)      
        self.address = Address(street, city, zipcode)

    def display_contact(self):
        print(f"Name: {self.person.name}")
        print(f"Age: {self.person.age}")
        print(f"Street: {self.address.street}")
        print(f"City: {self.address.city}")
        print(f"Zipcode: {self.address.zipcode}")

contact1 = Contact("Ankit", 20, "Pulchowk Rd", "Lalitpur", "44700")
contact1.display_contact()

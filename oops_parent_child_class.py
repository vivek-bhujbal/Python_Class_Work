'''
Inheritance is a fundamental concept in object -oriented programming (OOP)
that allows a class (child class) to inherit attributes and methods from
another class (parent class).
This promotes code reuse and helps struture progrms in a hierarchical manner.
syntax:
class ParentClass:
    # Parent class implementation

class ChildClass(ParentClass):
    # Child class implementation

'''

# Parent Class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Child class inheriting from animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Creating instances of child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the methods
print(dog.speak())
print(cat.speak())

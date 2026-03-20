# Polymorphism - The same method name behaves differently for different objects.

# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived class 1
class Dog(Animal):
    def speak(self):
        # overriding parent method
        print("Dog barks")

# Derived class 2
class Cat(Animal):
    def speak(self):
        # overriding parent method
        print("Cat meows")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]

for obj in animals:
    obj.speak()   # same method name, different behavior
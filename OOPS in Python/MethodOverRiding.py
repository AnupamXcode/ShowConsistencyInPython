# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")


# Child class 1
class Car(Vehicle):
    def start(self):
        # overriding parent method
        print("Car starts with a key")


# Child class 2
class Bike(Vehicle):
    def start(self):
        # overriding parent method
        print("Bike starts with a kick")


# Creating objects
v = Vehicle()
c = Car()
b = Bike()

# Calling same method on different objects
v.start()  # Parent method
c.start()  # Overridden method in Car
b.start()  # Overridden method in Bike


class Vehicle:
    def start(self):
        print("Vehicle base start")


class Car(Vehicle):
    def start(self):
        super().start()  # call parent method
        print("Car specific start")
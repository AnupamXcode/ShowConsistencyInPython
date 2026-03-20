class Animal:
    name1 = "Tiger"
class Human:
    name2 = "Akshat"

#Single Inheritance
class Mamba(Animal):
    name = "Snake"

# Multi Inheritance 
class Robot(Animal, Human):   
    name3 = "Charlie"

obj = Robot()
print(obj.name3)

class Funct:
    def __init__(self,name):
        pass

#-----------------------------------------------------------------------------------------------------------------------


## Multi Level Inheritance

# Base class (Level 1)
class Animal:
    def __init__(self, name):
        self.name = name  # attribute common to all animals

    def eat(self):
        print(f"{self.name} is eating.")


# Derived class from Animal (Level 2)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


# Further derived class from Dog (Level 3)
class Puppy(Dog):
    def weep(self):
        print(f"{self.name} is weeping.")


# Creating object of the lowest level class
puppy = Puppy("Tommy")

# Accessing methods from all levels
puppy.eat()   # inherited from Animal
puppy.bark()  # inherited from Dog
puppy.weep()  # defined in Puppy






class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips 
    

class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color
    
class Punefactory(BhopalFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets


# Animal class
class Animal:
    def move(self):
        print("The animal moves.")

# Dog class, inherits from Animal
class Dog(Animal):
    def move(self):
        print("The dog runs on four legs 🐕")

# Bird class, inherits from Animal
class Bird(Animal):
    def move(self):
        print("The bird flies through the sky 🦅")

# Vehicle class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Car class, inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")

# Plane class, inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")

# Create instances and call the move method
animal = Animal()
dog = Dog()
bird = Bird()

car = Car()
plane = Plane()

# Calling move() for different objects
animal.move()
dog.move()
bird.move()

car.move()
plane.move()

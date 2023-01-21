print("#////////////////////////////////////////////////////////////// 37. Module..........")
# module = a file containing python code. May contain function, classes, etc.
# Used with modular programming, which is to separate a program into parts

# import messages
# import messages as m
# from messages import hello,bye
# from messages import * (this one is dangerous) # 🟥 not efficient

# m.hello()
# m.bye()
# help("modules") # gives us list of built in modules
# documentation e giye python module index likheo search kora jete pare...

print("#////////////////////////////////////////////////////////////// 40. OOP..........")
# class Car:
#     pass
from module.car import Car

car_1 = Car("Car1", "Car1Company", 2021, "blue")
car_2 = Car("Car2", "Car2Company", 2022, "green")

car_1.drive()
car_1.stop()
print("car1 color : ", car_1.color)

car_1.wheels = 2
print("car1 wheels : ", car_1.wheels)
print("car2 wheels : ", car_2.wheels, "  which is default value")

# Car.wheels = 3 # ekhon shob object er wheel er value change hoye jabe ..

print("#////////////////////////////////////////////////////////////// 42. Inheritance..........")

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    # pass
    def run(self):
        print("This rabbit is running ... ")
class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print()
print("Rabit.Alive => ",rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()

print("#////////////////////////////////////////////////////////////// 43. Multilevel Inheritance..........")

# multi-level inheritance -> when a derived (child) class inherits another derived (child) class

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating ... ")

class Dog(Animal):
    def bark(self):
        print("This Dog is barking... ")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

print("#////////////////////////////////////////////////////////////// 44. Multiple Inheritance..........")

# multiple inheritance -> when a clild class is derived from more than one parent class

class Prey :
    def flee(self):
        print("This animal flees")
class Predator :
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Fish(Prey, Predator):
    pass

fish = Fish()
fish.flee()
fish.hunt()


print("#////////////////////////////////////////////////////////////// 45. Method Overriding..........")


class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()

print("#////////////////////////////////////////////////////////////// 46. Method Chaining..........")

# method chaining => calling multiple methods sequentially each call performs an action on the same
#     object and returns self

class Car:
    def turn_on(self):
        print("You start your engine")
        return self

    # method chaining korle self return kore dite hobe

    def drive(self):
        print("Go for drive")
        return self

    def brake(self):
        print("Breaking start")
        return self

    def turn_off(self):
        print("off you engine")
        return self


car = Car()

car.turn_on().drive()
car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()# \ is a line continuing character

print("#////////////////////////////////////////////////////////////// 47. super function..........")

# super() = Function used to give access to the methods of a parent class .
        # returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length * self.width
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(2,2)
cube = Cube(2,2,2)

print(cube.volume())
print(square.area())

print("#////////////////////////////////////////////////////////////// 48. abstract class..........")

# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class (comples mane baddho kore )

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation
# it's like an idea ....  structure .. mane ekta class er ki ki method lagbe .. shetar ekta list ..
# implementation ta shekhan e thake na .. implementation thake onno class e ...

from abc import ABC, abstractmethod # abc mane holo abstract base class
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    # go method ke na likhle error dekhabe
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motocycle")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()  # abstract class er object create kora jay na
car.go()
motorcycle.go()


print("#////////////////////////////////////////////////////////////// 49. Object as Argument..........")


























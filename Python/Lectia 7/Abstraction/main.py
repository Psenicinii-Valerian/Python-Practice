# Interface
# clasa abstracta, are doar metode abstracte, nu are atribute

# Clasa Abstracta
# Clasa abstracta, are minimum o metoda abstracta, poate sa contina mai multe metode obisnuite

# Orice interfata poate fi numita clasa abstracta, dar nu fiecare clasa abstracta poate fi numita interfata

from abc import ABC, abstractmethod
import math
# we can create abstract objects (instances of abstract classes/interfaces)
# all abstract methods must be overriden by chil classes
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def sleep(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Gaf Gaf")
#
#     def sleep(self):
#         print("Zzz")
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print("meow meow")
#
#     def sleep(self):
#         print("Zzz")
#
#
# dog = Dog()
# cat = Cat()
# dog.make_sound()
# dog.sleep()

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        print("abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width * self.height)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * (math.pi * self.r)
    def area(self):
        return math.pi * self.r ** 2

rect = Rectangle(10,20)
print(rect.perimeter())
circle = Circle(23)
print(round(circle.area(), 2))
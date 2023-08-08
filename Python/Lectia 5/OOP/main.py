# from car import Car
#
# car1 = Car("Toyota", "Supra", 1998, "Purple")
# car1.color = "Yellow"
#
# car2 = Car("Nissan", "Skyline", 1994, "Blue")
#
# car2.drive()
# car1.stop()
#
# # Car.drive(car2)
# # print(car2.wheels)
# # print(Car.wheels)
# # print(car2.model)
# # print(car1.color)

# from  bank_account import BankAccount
# acc1 = BankAccount("312331203", 900)
# acc1.display_balance()
# acc1.deposit(200)
# acc1.display_balance()
# acc1.withdraw(1300)
# acc1.display_balance()
# acc1.deposit(100)
# acc1.display_balance()
# acc1.withdraw(1000)
# acc1.display_balance()

# # Super Class = Parent Class
# # Single Inheritance
# class Animal:
#     alive = True
#
#     def eat(self):
#         print("Neam neam")
#     def sleep(self):
#         print("ZZZZZZ")
#
# class Cat(Animal):
#     def faramarea_mobilei(self):
#         print("Eu faram patul")
#
# class Shark(Animal):
#     def swim(self):
#         print("Eu rechin eu swimez")
#
# class Flamingo(Animal):
#     def fly(self):
#         print("Eu flyesc")
#
# # Super class doesn't have access to child's methods/attributes, while child classes have
# # Each child class has their own methods and don't have access to each other implementations
# animal = Animal()
# animal.sleep()
#
# cat = Cat()
# cat.faramarea_mobilei()
#
# shark = Shark()
# shark.swim()
#
# flami = Flamingo()
# flami.fly()

# # Multilevel Inheritance
# class Organism:
#     alive = True
#
# class Animal(Organism):
#     def eat(self):
#         print("eat eat")
#     def sleep(self):
#         print("sleep sleep")
#
# class Cat(Animal):
#     def go_latok(self):
#         print("Ma duc in latok")
#
# class SiamskiiMotan(Cat):
#     def minus_zarplata(self):
#         print("Eu cost cat un rinichi")
#
# class Plant(Organism):
#     def fotosinteza(self):
#         print("Fotosinteza")
#
# cat = Cat()
# print(cat.alive)
# cat.sleep()
# cat.go_latok()
#
# siam = SiamskiiMotan()
# siam.minus_zarplata()

# # Multiple Inheritance
# class Animal:
#     alive = True
#
# class Cat:
#     def get_cat(self):
#         print("eu-s motan")
#     def eat(self):
#         print("eus motan eu mananc")
#
# class Tigru(Cat, Animal):
#     def hunt(self):
#         print("tigrul hunteaza")
#     def eat(self):
#         print("eus tigru eu mananc")
#
#
# tigr = Tigru()
# tigr.get_cat()
# tigr.hunt()
# tigr.eat()

# # super() method
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         print(f"Area = {self.width * self.height}")
#
# class Square(Rectangle):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#     def get_area(self):
#         print("Get area for square:")
#         super().get_area()
#
# rect = Rectangle(5, 10)
# rect.get_area()
# kvadrat = Square(10, 10)
# kvadrat.get_area()

# class Transport,fuel_type,start_engine()
# Car,Motorcycle super.start_engine(),fuel_type
# Car wheels,Moto has_sidecar
class Transport:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    def start_engine(self):
        print("Vrum Vrum!")

class Car(Transport):
    wheels = 4
    def __init__(self, fuel_type):
        super().__init__(fuel_type)
    def start_engine(self):
        print("Starting engine for Car")
        super().start_engine()

class Motorcycle(Transport):
    fuel_type = "gasoline"
    wheels = 2
    def __init__(self, fuel_type, has_sidecar):
        super().__init__(fuel_type)
        self.has_sidecar = has_sidecar
    def start_engine(self):
        print("Starting engine for Motorcycle")
        super().start_engine()

print("******************TRANSPORT******************")
transport = Transport("electricity")
print(f"Fuel type: {transport.fuel_type}")
transport.start_engine()

print("\n******************CAR******************")
car = Car("diesel")
print(f"Fuel type: {car.fuel_type}")
car.start_engine()
print(f"Wheels amount: {car.wheels}")

print("\n******************MOTORCYCLE******************")
moto = Motorcycle("gasoline", True)
print(f"Fuel type: {moto.fuel_type}")
moto.start_engine()
print(f"Has sidecar: {'yes' if moto.has_sidecar == True else 'no'}")
if moto.has_sidecar == True:
    moto.wheels = 5
print(f"Wheels amount: {moto.wheels}")

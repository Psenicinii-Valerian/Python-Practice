# class Confectionary:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def describe(self):
#         print(f"{self.name} is sold at price {self.price} BTC/kg")
#
# class Tortik(Confectionary):
#     def describe(self):
#         print(f"Tortikul: {self.name} costs {self.price} EPH/kg")
#
# class Candy(Confectionary):
#     def describe(self):
#         print(f"Kanfetka: {self.name} costs {self.price} XRP/kg")
#
# class Cookie(Confectionary):
#     # keyword pass = skip
#     pass
#
# tort = Tortik("Napoleon", 1200)
# candy = Candy("Meteorit", 8000)
# cookie = Cookie("Abicinie cu Ciocolata", 250)

# tort:Confectionary.describe(tort)
# tort.describe()
# candy.describe()
# cookie.describe()

# class Beverage:
#     def __init__(self, name, size, price):
#         self._name = name
#         self._size = size
#         self._price = price
#
#     def get_name(self):
#         return self._name
#     def get_size(self):
#         return self._size
#     def get_price(self):
#         return self._price
#     def set_price(self, price):
#         self._price = price
#     def describe(self):
#         return f"{self._size}l of {self._name} costs {self._price} lei"
#
# class Soda(Beverage):
#     def __init__(self, name, size, price, flavour):
#         super().__init__(name, size, price)
#         self._flavour = flavour
#     def set_flavour(self, flavour):
#         self._flavour = flavour
#     def describe(self):
#         return f"{self._size}l of {self._name} soda costs {self._price} lei and has the taste of {self._flavour}"
#
# class DietSoda(Soda):
#     def __init__(self, name, size, price, flavour):
#         super().__init__(name, size, price, flavour)
#     def describe(self):
#         return f"{self._size}l of {self._name} diet soda costs {self._price} lei and has the taste of {self._flavour}"
#
# regular_soda = Soda("Sprite", 0.33, 20, "Cucumber")
# print(regular_soda.describe())
#
# diet_soda = DietSoda("CocaCola Zero", 0.33, 22, "Lime")
# print(diet_soda.describe())
#
# regular_soda = Soda("Fanta", 0.75, 24, "Mystery")
# print(regular_soda.describe())

class Aircraft:
    def __init__(self, model, manufacturer, capacity):
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity

class PassengerAircraft(Aircraft):
    def fly(self):
        print(f"Passenger Aircraft model {self.model} manufactured by {self.manufacturer} with the capacity {self.capacity} currently flies")

class CargoAircraft(Aircraft):
    def fly(self):
        print(f"Cargo Aircraft model {self.model} manufactured by {self.manufacturer} with the capacity {self.capacity} currently flies")

class Airport:
    aircrafts = []
    def __init__(self, aircrafts):
        for aircraft in aircrafts:
            self.aircrafts.append(aircraft)

pass_aircraft1 = PassengerAircraft("A330-300", "Airbus", 200)
pass_aircraft2 = PassengerAircraft("777-300", "Boeing", 250)
pass_aircraft3 = PassengerAircraft("747-8", "Boeing", 170)

cargo_aircraft2 = CargoAircraft("An-22", "Antonov", 500)
cargo_aircraft3 = CargoAircraft("Y-20", "Xi'an", 444)

airport = Airport([pass_aircraft1, pass_aircraft2, pass_aircraft3, cargo_aircraft2, cargo_aircraft3])

for aircraft in airport.aircrafts:
    aircraft.fly()
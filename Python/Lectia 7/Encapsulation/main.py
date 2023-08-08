class MyClass:
    def __init__(self):
        self.number = 12        # public field
        self.__number2 = 24     # private field - poate fi accesat doar dinauntrul clasei
        self._number3 = 49      # protected field

    def get_number2(self):
        return self.__number2

    def get_number3(self):
        return self._number3

    def set_number2(self, number2):
        self.__number2 = number2

    def set_number3(self, number3):
        self._number3 = number3

    def __metoda(self):
        print("ia privat")

                                                    # Name Mangling
# Name Mangling - procesul specific Python-ului care ne permite sa ignoram/ocolim modificatorii de acces
# NU FOLOSIM Name Mangling!
obj = MyClass()
print(obj.number)
# print(obj.__number2)
# print(obj._number3)
# obj._MyClass__number2 = 23
# print(obj._MyClass__number2)
# obj._MyClass__metoda()
print(obj.get_number3())
obj.set_number3(3123213)
print(obj.get_number3())

a = getattr(obj, "_MyClass__number2")
print(a)

b = getattr(obj, "_MyClass__metoda")
b()


# def add():
#     print("add function")
#
# v = add
# v()



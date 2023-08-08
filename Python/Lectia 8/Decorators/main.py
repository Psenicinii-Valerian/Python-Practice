                                                    # Decorators
                                                    # Decorator 1
# def decor(func):
#     def inner(*args, **kwargs):
#         print("<h1>")
#         func(*args, **kwargs)
#         print("</h1>")
#     return inner
#
# @decor
# def use_decor(n1, n2, n3, n4, n5):
#     print(n1, n2, n3, n4, n5)
#
# use_decor(100, 200, 300, 400, 500)
#
# @decor
# def summ(x, y, z, z1):
#     print(x+y+z+z1)
#
# summ(10, 20, 30, 50)

                                                    # Decorator 2
# def uppercase_decorator(func):
#     # un exemplu de a transmite parametrul functiei ca string
#     def wrapper(text: str):
#         # aici programul ne va autocompleta metoda text.upper()
#         # deoarece se cunoaste faptul ca text este o variabila de tip string
#         # => se stiu metodele ce pot fi aplicate asupra acesteia
#         result = func(text.upper())
#         return result
#     return wrapper
#
# @uppercase_decorator
# def greet(name):
#     return f"Zdarova, {name}"
#
# result = greet("erjan")
# result2 = greet("vanea")
#
# print(result2)
# print(result)

                                                    # Decorator 3
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function with name {func.__name__} and with arguments {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @log_decorator
# def multiply(a, b):
#     return a * b
#
# result = multiply(5, 3)
# print(result)

                                                    # Decorator 4
# def repeat_decorator(repeat_times):
#     def decorator(func):
#         def wrapper():
#             # _ - iterator gol, care nu se foloseste in parcurgerea for-ului
#             for _ in range(repeat_times):
#                 func()
#         return wrapper
#     return decorator
#
# # repeat_times - keyword care indica denumirea parametrului caruia ii dam valoare (4)
# @repeat_decorator(repeat_times=4)
# def say_hi():
#     print("zdarova")
#
# say_hi()

                                                    # Decorator 5
# def uppercase_decorator(prefix):
#     def decorator(func):
#         # un alt exemplu de a indica parametrul unei functii ca string:
#         def wrapper(text):
#             # aici va trebui sa scriem de mana text.upper()
#             # asta se intampla pentru ca programul nu stie
#             # ce tip de data e text => nu se stiu metode pentru acesta
#             result = func(text.upper())
#             return f"{prefix} {result}"
#         return wrapper
#     return decorator
#
# @uppercase_decorator(prefix="!!!!!")
# def greet(name):
#     return f"Zdarova, {name}"
#
# result = greet("erjan")
# print(result)

#decorator pentru sortarea unei colectii
#decorator unique characters

def collection_sort_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@collection_sort_decorator
def sort_collection(numbers: list):
    numbers.sort()
    return numbers

result = sort_collection([5, 10, 8, 2, -5, 99])
print(f"Sorted collection: {result}")


def unique_characters_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = list(result)
        result.sort()
        return result
    return wrapper

@unique_characters_decorator
def unique_characters_selector(characters: list):
    characters = set(characters)
    return characters

result = unique_characters_selector(['a', 'b', 'b', 'c', 'g', 'z', 'e', 'e', 'z', 'a'])
print(f"Unique characters list: {result}")
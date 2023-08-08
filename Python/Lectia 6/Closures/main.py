# Superior rank functions

# def higher_func(function):
#     return function(10)
#
# def multiply(x):
#     return x * x
# def power(x):
#     return x ** x
# def add(x):
#     return x + x
#
# m = higher_func(multiply)
# p = higher_func(power)
# a = higher_func(add)
#
# print(m, p, a)

# # Closures - a nested function that allows us to access variables of the outer function even after the outer function is closed
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
# closure = outer(10)     # closure = inner(y)
# print(closure(5))
#
# def hello():
#     print("Hello World!")
#     def world(a, b, c):
#         return a + ' ' +  b + ' ' +c
#     return world
#
# closure2 = hello()
# print(closure2("Moldova", "Chisinau", "Bulboaca"))

# # Global scope - used to access and modify global variables from within a function
# x = 10
# def printt():
#     global x
#     print(x)
#     x = 15
#
# printt()
# print(x)
#
# idnp = 11
# def show_idnp():
#     global idnp
#     print(idnp)
#     idnp += 10
#
# show_idnp()
# print(idnp)

# # Non local - used to access and modify variables from the nearest enclosing scope that is not global
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 2
        print("inner x =", x)
    inner()
    print("outer x =", x)

outer()

# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
#
# c = counter()
# for i in range(10):
#     print(c())
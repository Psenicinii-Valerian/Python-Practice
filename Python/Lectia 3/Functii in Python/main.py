# def greeting(name):
#     print("Hello " + name)
#
# def sum_numbers(a, b):
#     print(a+b)
#
# sum_numbers(1, 2)
# sum_numbers(2, 4)
# sum_numbers(10, 22)
# sum_numbers(33, 101)

# def multiply_numbers(a, b=2):
#     print(a*b)
#
# multiply_numbers(3, 3)

# 1) find average number
# 2) find max of a list

# # ex 1
# def find_average(numbers):
#     print(f"Average of the given numbers: {sum(numbers) / len(numbers)}")
#
# # ex 2
# def find_max(numbers):
#     print(f"Max of the given numbers: {max(numbers)}")
#
# numbers = [10, 20, 4, 5, 6]
# find_average(numbers)
# find_max(numbers)
# def greeting(firstname, lastname, patronymic):
#     print(f"Hello {firstname} {lastname} {patronymic}")
#
# # keyword arguments - we explicitly indicate the parameters for the values when we call the function
# greeting(patronymic="Vitalie", firstname="Daniil", lastname="Chitic")

                                            # Args and Kwargs
# # *args = tuple
# def print_arg(*args):
#     for i in args:
#         print(i)
#
# print_arg("apple", "banana", "cherry")

# # **kwargs = dict
# def print_kwargs(**kwargs):
#     for key, val in kwargs.items():
#         print(key + ":", val)
#
# print_kwargs(name="Daniil", age=35, city="Tokyo")

# def print_pet_names(owner, **pets):
#     print(f"Owner name : {owner}")
#     for pet, name in pets.items():
#         print(f"{pet}: {name}")
#
# print_pet_names("Daniil", dog="Doberman", fish=["Garik", "Iarik", "Valik"], snake="Anaconda")

#                                           # Lambda functions
# # lambda = anonymous functions
# summ = lambda x,y: x+y
# multiply = lambda x,y: x*y
# add =  lambda x,y,z: x+y+z
# full_name = lambda firstname, lastname, patronymic: firstname + " " + lastname + " " + patronymic
#
# print(summ(5, 3))
# print(multiply(5, 3))
# print(add(1, 2, 3))
# print(full_name("Daniil", "Chitic", "Vitalie"))

# # 1) calcularea sumei dintr-un arg
# # 2) calcularea sumei produsului dintr-un kwarg: counter, product, cantitatea
# # 3) primeste list si inmulteste fiecare numar cu 5
#
# def sum_arg(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(f"Total sum: {sum}")
#
# sum_arg(1, 2, 3, 4, 5)
#
# def sum_products(counter=0, *quantity, **kwargs):
#     item = 0
#     total = 0
#     for i in quantity:
#         price = 0
#         for key, cost in kwargs.items():
#             price = cost * i[item]
#             print(f"Price of {i[item]} x {key}s: {price}$$")
#             total += price
#             item += 1
#     return total
#
# print(f"Total price of the specified products: {sum_products(0, (3, 4, 2), tshirt=200, dress=400, shirt=150)}$$")
#
# list_multiply = lambda numbers: [num*5 for num in numbers]
# numbers = [3, 6, 2, 8]
#
# print(list_multiply(numbers))
#
# # professor solve for task 2
# def calculate_product(**kwargs):
#     total_cost = 0
#     for product, quantity in kwargs.items():
#         price = products.get(product)
#         total_cost += price * quantity
#     return total_cost
#
# products = {'apple': 1.0, 'banana': 0.5, 'orange': 1.2}
# total = calculate_product(apple=3, banana=2, orange=1)
# print(total)

#                                             # Recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# print(factorial(5))
#
# def reverse(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         reverse(n-1)
#
# print(reverse(10))
#
# def sum_list(lst):
#     if len(lst) == 0:
#         return 0
#     else:
#         return lst[0] + sum(lst[1:])
#
# print(sum_list([1, 2, 3, 4, 5]))

# # find max number in a list
# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_rest = find_max(lst[1:])
#         return lst[0] if lst[0] > max_rest else max_rest
#
# print(find_max([1, 2, 50, 43, 0]))

                                            # LOOPS
# 1) for in
# fruits = ["apple", "banana", "mandarinka"]
# for fruit in fruits:
#     print(fruit)

# 1.1) for in enumerate
# cars = ["Honda", "Ferrari", "Vazik"]
# for index, car in enumerate(cars):
#     print(str(index+1) + ") " + car)

# name = "Daniil"
# for letter in name:
#     print(letter)

# 2) while
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# 3) do while
while True:
    response = input("Input 'w' for exit: ")
    if response == 'w':
        break


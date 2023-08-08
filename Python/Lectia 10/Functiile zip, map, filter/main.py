                                                        # MAP
# map - functie care itereaza printr-o colectie si foloseste pentru fiecare element dinauntrul sau o oarecare functie
# aceasta functie o indicam tot noi ca primul parametru, dandu-i doar signatura functiei (adica nu o apelam cu ())
# map returneaza un iterator (map object - adresa colectiei), deci o putem impacheta intr-un list si sa il afisam

#                                                         # Sample 1
# a = [-1, -2, -3, -4, -5]
# result = list(map(abs, a))
# print(result)
#
#                                                         # Sample 2
# def f(x):
#     return x**2
#
# b = [1, 2, 3, 4, 5]
# result2 = list(map(f, b))
# print(result2)
#
#                                                         # Sample 3
# c = ["piton", "andrei", "lorem", "html"]
# result3 = list(map(lambda x: x[::-1], c))
# print(result3)
#
#                                                         # Sample 4
# d = ["piton", "andrei", "lorem", "html"]
# result4 = list(map(len, d))
# print(result4)
#
#                                                         # Sample 5
# e = ["piton", "andrei", "lorem", "html"]
# result5 = list(map(str.upper, e))
# print(result5)
#
#                                                         # Sample 6
# f = ["piton", "andrei", "lorem", "html"]
# result6 = list(map(list, f))
# # sorted - metoda universala de sort (pentru orice tip de date)
# sorted = list(map(sorted, result6))
# print(sorted)
#
#                                                         # Sample 7
# s = list(map(int, input("Enter numbers: ").split()))
# print(s)

#                                                         # Practice 1
#
# # 1. creati functia pentru socotirea caracterelor
# # a = ["hello","python"]
# # [{'h': 1,'e':1,'l':2}]
# # 2. folositi functia creata pentru fiecare element din colectie
#
# def count_letter_appearance(string):
#     appearances = {}
#     for i in string:
#         appearances[i] = string.count(i)
#
#     return appearances
#
# # main
# string = ["hello", "python"]
# string_letter_appearance = list(map(count_letter_appearance, string))
# print(string_letter_appearance)
#
#                                                         # Another way to solve
# # def count(lista):
# #     res = list(map(lambda cuvant: {caracter: cuvant.count(caracter) for caracter in set(cuvant)}, lista))
# #     return res
# # listaCuv = ["hello", "python"]
# # res = count(listaCuv)
# # print(res)


#                                                         # Filter
# # filter - functie care itereaza prin intreaga colectie si salveaza elementele care dupa conditie
# # (care noi o transmitem ca primul parametru) corespund rezultatului de True
#
#                                                         # Sample 1
# def f(x):
#     return x > 10;
#
# a = [0, 30, 143124, 213, 3, 4, 213, 43]
# b = list(filter(f, a))
# print(b)
#
#                                                         # Sample 2
# a = ["word", "me", "python", "ad", "abracadabra", "darksouls", "sekiro"]
# b = list(filter(lambda x: len(x) < 5, a))
# print(b)
#
#                                                         # Sample 3
# a = "3543asdbsDgsdg3214";
# b = (list(filter(str.isdigit, a)))
# print(b)
#
#                                                         # Sample 4
# d = {
#     "Iphone XR": 7000,
#     "Iphone 12": 15000,
#     "Iphone 14 Pro Max": 42000,
#     "Iphone 4s": 2500,
# }
#
# b = list(filter(lambda x: d[x] < 10000, d))
# b1 = list(filter(lambda x: d[x] > 10000, d))
# print(b, b1)

#                                                         # Practice 1
# def is_prime(number):
#     is_prime = True
#     if number < 2:
#         is_prime = False
#     for i in range(2, number//2+1):
#         if number % i == 0:
#             is_prime = False
#             break
#     return is_prime
#
#
# def is_palindrome(number):
#     is_palindrome = False
#     if str(number) == str(number)[::-1] and len(str(number)) > 1:
#         is_palindrome = True
#
#     return is_palindrome
#
# # main
# numbers = [2, 3, 4, 5, 7, 8, 9, 10, 11, 22, 23, 24, 101, 2, 3, 5, 7, 11, 22, 101]
# verified = list(filter(lambda x: is_prime(x) and is_palindrome(x), numbers))
# print(verified)
#
#
#                                                        # Practice 2
# words = ["hello", "bunaziuahellozdrastvuite", "guttenmorgencomdrade", "helloworldpython", "Marcus Rashford"]
# verified = list(filter(lambda x: len(x) > 10, words))
# print(verified)


                                                        # Zip
# zip - functie care combina elementele dintr-o colectie cu elementele din celelalte colectii, creand perechi noi

                                                        # Sample 1
# in momentul in care unuia din elemente dintr-o colectie nu i se gaseste pereche, acesta va fi omis
# astfel, daca avem o lista de 4 elemente si o alta lista de 6 elemente => vor fi create 4 doar perechi
a = [1, 2, 3, 4, 5]
b = [100, 200, 300, 400]

# for i in range(4):
#     print(a[i], b[i])

# iteratorii pot fi iterati doar o data
# result = zip(a, b)
# for i in result:
#     print(i)
# print(result)
# for i in result:
#     print(i)

# Impachetare/Packing
result = list(zip(a, b))
print(result)

                                                        # Sample 2
a = [1, 2, 3, 4, 5]
b = [100, 200, 300, 400, 500]
c = 'abcd'
result = list(zip(a, b, c))
print(result)

                                                        # Sample 3
# Despachetare a unui list
data = [(1, 'A'), (2, 'B'), (3, 'C')]
numbers, letters = zip(*data)
print(list(numbers))
print(letters)

# Despachetare/Unpacking a unui zip obisnuit
a = [1, 2, 3, 4, 5]
b = [100, 200, 300, 400, 500]
c = 'abcd'
result = zip(a, b, c)
print(result)

num1, num2, num3 = zip(*result)
print(num1, num2, num3)
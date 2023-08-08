                                                        # Sample 1
# def f():
#     return [43, 321, 4324, 12341, 321]
#
# def genf():
#     for i in [43, 321, 4324, 12341, 321]:
#         # yield - fratele-geaman a lui return, doar ca dupa ce acesta returneaza o valoare
#         # el se ingheata si asteapta sa se execute urmatorul pas ca sa mearga mai departe
#         # de la momentul in care acesta s-a oprit
#         yield i
#
# print(next(genf()))
# print(next(genf()))
# print(next(genf()))
# print("-------------")
# s = genf()
# print(next(s))
# print(next(s))
# print(next(s))
#
# for i in s:
#     print("for", i)

                                                        # Sample 2
# def genf():
#     s = 7
#     for i in [43, 321, 4324, 12341, 321]:
#
#         yield i     # SE OPRESTE PANA LA APELAREA URMATORII VALORI A GENERATORULUI PRIN NEXT()
#         print("s:", s)
#         s = s*10+7
#
# g = genf()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

                                                        # Sample 3
import sys
sys.set_int_max_str_digits(0)

def fact(n):
    pr = 1
    a = []
    for i in range(1, n+1):
        pr = pr * i
        yield pr

for i in fact(1000):
    print(i, end=' ')


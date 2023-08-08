                                                        # Generators
# Generator - un obiect ce de fapt reprezinta un iterator
# Generatoarele se folosesc cand avem nevoie de viteza executarii codului
# nu exista Tuple Comprehension in Python
# generatoarele pot fi iterate doar o data
# generatoarele pastreaza in sine valori doar pentru 1 pas (returneaza doar cate o valoare)
# functia next ca si in general iterarea generatoarelor se calculeaza live (in momentul executiei)

                                                        # Sample 1
# a = (i**2 for i in range(1, 53312321312321))
# # a = i(for) + list
# # next(a) - returneaza fiecare ultima valoare dupa fiecare pas
# # =>: pentru a afisa 1 valoare putem da next(a), ulterior a 2 valoare tot cu next(a) ...
# # pentru a afisa deodata tot generatorul il putem itera
# for i in a:
#     print(i)

                                                        # Sample 2
# gen = (x for x in range (0,11) if x % 2 == 0)
# print(next(gen))    #0
# print(next(gen))    #1
# for i in gen:
#     print("for", i)

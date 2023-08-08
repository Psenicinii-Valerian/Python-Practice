                                    # from collections import namedtuple
# #namedtuple - mix(soleanka) dintre OOP clase + kwargs + tuple
#
# # Person - denumirea tuplului (ca clasa)
# # name, age - proprietati
# Person = namedtuple("Person", ["name", "age"], defaults=["BibaBoba", 10])
# person1 = Person(name="Andrei", age=58)
# person2 = Person(name="Mishanea", age=20)
# person3 = person1 + person2
# # person1.name = "Misha"    eroare din cauza ca nu putem modifica tuple
# print(person3)
# print(type(person3))
#
# tpl1 = (1, 2, 3)
# tpl2 = (10, 20, 30)
# tpl3 = tpl1 + tpl2
# print(tpl3)
#
# person4 = Person() # daca vom incerca sa cream un obiect gol,
# # vom primi automat numele si varsta ce vor avea valorile din default(de asta este important sa setam defaultul)
# print(person4)


                                    # from collections import defaultdict

# d = {
#     "fruits": ["apple", "banana"]
# }
# print(d["vegetables"]) # error pentru ca nu avem cheia vegetables in dictionarul d

# d = defaultdict(set)
# d["fruits"].add("apple")
# d["fruits"].add("banana")
# print(d["fruits"]) # nu vom avea eroare, se va adauga un nou set gol pentru cheia vegetables

# d = defaultdict(list)
# d["fruits"].append("apple")
# d["fruits"].append("banana")
# print(d["vegetables"]) # nu vom avea eroare, se va adauga un nou list gol pentru cheia vegetables
# print(d)


                                    # from collections import Counter
#
# lst = ["ferrari", "honda", "honda", "mustang", "ferrari", "vazik", "kapeika", "ferrari"]
# counterLst = Counter(lst)
# print(counterLst["honda"])
# print(counterLst["lamborghini"]) # daca nu gaseste elementul, va returna 0 (nu eroare)
#
# setik = {"ferrari", "honda", "honda", "mustang", "ferrari", "vazik", "kapeika", "ferrari"}
# counterSetik = Counter(setik)
# print(counterSetik)
#
# dict = {"ferrari": 3, "ferrari": 5}
# counterDict = Counter(dict)
# print(counterDict)


                                    # from collections import deque
# # deque - double ended que
#
# deq = deque()
# deq.append("apple")
# deq.append("banana")
# deq.append("orange") # va adauga elementul la sfarsit de deque
# deq.appendleft("grape") # va adauga elementul la inceput de deque
# deq.appendleft("pipet de pui")
# print(deq)
# deq.pop() # va sterge ultimul element din deque
# deq.popleft() # va sterge primul element din deque
# print(deq)


                                    # from collections import ChainMap
#
# dict1 = {"crevetci": 5, "calmari": 10}
# dict2 = {"calmari": 2, "peste abicnii": 4}
# print(dict2)
#
# chain_map = ChainMap(dict1, dict2)
# print(chain_map)
# print(chain_map["crevetci"])
# print(chain_map["calmari"])
# print(chain_map["calmari"])
# print(chain_map["peste abicnii"])
# print(dict1)


# Counter from collections
# merge_and_count_lists(lists)
from collections import Counter


def merge_and_count_lists(lists):
    arr = [num for list in lists for num in list]
    return Counter(arr)


matrix = [[1, 2, 3], [2, 342, 423], [342, 523]] # -> [] de cate ori fiecare element se gaseste
print(merge_and_count_lists(matrix))


# count_characers_frequency(string)
# calculati de cate ori se intalneste fiecare cuvant in string cu ajutrul lui Counter


def count_characters_frequency(string):
    return Counter(string)


capitals = ["London", "Paris", "Tokyo", "Rome", "Paris", "Madrid", "Beijing", "Moscow", "London",
            "New Delhi", "Tokyo", "Paris", "Tokyo", "Berlin", "Madrid"]
print(count_characters_frequency(capitals))

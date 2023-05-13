# my_list = [1, 2, 3, True, "Hello"]
# print(my_list)
# my_list[0] = "haha"
# print(my_list)

                                                    # LIST
# lists are a collection of elements which is mutable and organized
# list_name = [values]
# my_list = [1, 10, 23, 5, 3, 123, "Hello"]
# print(len(my_list))
# my_list.append(4)       # list.append(val) - add a new element in the end of the list
# my_list.insert(0, 10)   # list.insert(index, val) - add a new element on the index position
# my_list.remove("Hello") # list.remove(value) - removes a searchable element from list
# my_list.reverse()       # list.reverse() - turns a list backwards
# my_list.sort()          # list.sort() - sorts the list in ascending order
# print(my_list)
# my_list.clear()         # list.clear() - removes data from list
# print(my_list)

                                                    # TUPLE
# tuples are immutable and organized
# tuple_name = (values)
# my_tuple = (1, 2, 3, 4, 1, 1)
# v = my_tuple.count(1)           # tuple_name.count(val) - counts how much a searchable element appears in the tuple
# v = my_tuple.index(3)           # tuple_name.index(val) - returns the first index encounter of a searchable element
# print(my_tuple)
# print(v)

# a = (1, 2, [10, 20], 4)         # you can hold/change changeable element insde of immutable tuple
# print(a[2])
# a[2].append(200)
# print(a)

# a = (1, 2, 3)
# b = [1, 2, 3]
# c = {}
#
# c[a] = "Hello"
# print(c)
#
# # c[b] = "Hi"       # error
# # print(c)
#
# a = (1, 2, 3)
# a = list(a)         # tuples can be transformed in lists and back
# a.append(100)
# a.reverse()
# a = tuple(a)
# print(a)
                                                    # SET
# sets are unorganized and unique
# set_name = {values}
# mouses = {"HyperX", "Razer", "Logitech", "Ofisnaia", "Razer", "Razer"}
# keyboards = {"Ofisnaia", "Akko", "Varmillo", "DarkProject"}
# mouses.add("JBL")                         # set_name.add(val) - add a new element
# mouses.remove("Ofisnaia")                 # set_name.remove(val) - removes searchable value from set
# mouses.clear()                            # set_name.clear() - clears all the data from set
# peripheral = mouses.intersection(keyboards) # set_name3 = set_name1.instersection(set_name2) - find elements that intersects in both sets and return them
# keyboards.update(mouses)                    # set_name1.update(set_name2) - add all the data from the second set to first
# peripheral = mouses.union(keyboards)        # set_name3 = set_name1.union(set_name2) - unites 2 sets in one
# peripheral = mouses.difference(keyboards)   # set_name3 = set_name1.difference(set_name2) - returns the difference between first and second set
# print(mouses)
# print(keyboards)
# print(peripheral)
                                                    # DICTIONARY
# contains a pair of (key: value) and are unordered
# inside a dictionary, as a key we can have a tuple (unchangeable, immutable element) (we can't have list as a key)
# dict_name = {
#            "key1":"value1",
#            "key2":"value2"
# }

# my_dict = {
#     "name": ("John", "Mike"),
#     "surname": "Smith",
#     "age": 18,
#     "gender": "male"
# }
# for key, value in my_dict.items():
#     print(f"{key} : {value}")

capitals = {
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Moldova": "Chisinau",
    "USA": "Washington DC"
}
print(capitals)
capitals.update({"Israel": "Jerusalem"})        # dict_name.update({"key":"value"}) - update value of searchable key or creates a new pair of key-value
print(capitals.keys())                          # dict_name.keys() - returns keys of a dictionary
print(capitals.values())                        # dict_name.values() - returns values of a dictionary
capitals.pop("Germany")                         # dict_name.pop("key") - removes the pair key-value from the dictionary by searching it with key
print(capitals)
v = capitals.get("USA")                         # dict_name.get("key") - returns the value of a pair by searchable key
print(v)
# capitals.clear()
# print(capitals)                                 # dict_name.clear() - deletes all the data from dictionary
print(capitals.items())                         # dict_name.items() - returns pairs from dictionary

for key, val in capitals.items():
    print(f"{key}: {val}")
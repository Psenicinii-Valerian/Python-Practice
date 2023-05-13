# 1) Calculati cantitatea elementelor unice din List
def unique_list_elem_number(lst):
    result = [lst[0]]
    for i in lst[1:]:
        unique = True
        for elem in result:
            if i == elem:
                unique = False
                break
        if unique:
            result.append(i)
    print(f"There are: {len(result)} unique elements in the specified list")

list1 = [1, 2, 2, 5, 8, 4, 4, 8]
unique_list_elem_number(list1)

# 2) Intoarceti un Tuple invers
def reverse_tuple(tuple1):
    tpl = list(tuple1)
    tpl.reverse()
    tpl = tuple(tpl)
    print(tpl)

tuple1 = (10, 20, 30, 40, 50)
reverse_tuple(tuple1)

# 3) Calculati suma elementelor din Tuple trecand prin el cu for-loop
def tuple_sum(tuple2):
    sum = 0
    elem = 0
    for i in tuple2:
        sum += i
    return sum

tuple2 = (1, 2, 4)
print(tuple_sum(tuple2))

# 4) Selectati numai elemente unice din doua Set:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# set-ul mereu are numai elemente unice, deci numai trebuie sa unesc primul set cu al doilea
set1 = set1.union(set2)
print(set1)

# 5) Stergeti o lista de chei-valori din dictionar
def remove_dictionary_items_by_key(keys, dict):
    to_delete = []
    for key, value in dict.items():
        for i in keys:
            if i == key:
                to_delete.append(key)
    for elem in to_delete:
        del dict[elem]

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]

remove_dictionary_items_by_key(keys, sample_dict)
print(sample_dict)


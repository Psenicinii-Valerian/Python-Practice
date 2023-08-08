                                                        # TASK 1
# list_items = []
#
# def add_list_items(item):
#     global list_items
#     list_items.append(item)
#
# for i in range(4):
#     item = input(f"Enter the {i+1} item you want to add to your list: ")
#     add_list_items(item)
#
# print("\nShowing list items:")
# i = 1
# for item in list_items:
#     print(f"List item[{i}]: {item}")
#     i+=1

                                                        # TASK 2
# fruits = []
# def outer_func(fruit):
#     global fruits
#     fruits.append(fruit)
#     inner_list = fruits.copy()
#     def inner_func():
#         nonlocal inner_list
#         return inner_list
#     inner_func()
#     return inner_func
#
# try:
#     print(inner_list)
# except NameError as e:
#     print("Cannot print a nonlocal variable! You solevoi...")
#
# add_fruit1 = outer_func("apple")
# add_fruit2 = outer_func("banana")
#
# show_fruits = add_fruit2
# i = 1
# for fruit in show_fruits():
#     print(f"List inner_list[{i}]: {fruit}")
#     i+=1
#
# i = 1
# for fruit in fruits:
#     print(f"List fruit[{i}]: {fruit}")
#     i+=1

                                                        # TASK 3
def outer_func():
    dict = {}
    def inner_func():
        for i in range(3):
            key = input(f"Enter your dictionary {i+1} key: ")
            value = input(f"Enter your dictionary {i+1} value: ")
            dict.update({key: value})
        print("\nDictionary display:")
        for key, value in dict.items():
            print(f"{key}: {value}")
        # 2 variant to show
        # for key in dict:
        #     print(f"{key}: {dict[key]}")
    return inner_func

dict_insertion = outer_func()
dict_insertion()
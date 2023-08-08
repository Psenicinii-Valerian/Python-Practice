                                            # Processing exceptions
### structure
# try:
#    # 5/2
# except ErrorName:
#    # code to verify if contains exceptions
# else:
#    # code that executes when no exception occurs
# finally:
#    # code that always executes

# CTRL + CTRL(Hold down) + Downwards arrow - select more lines at the same time
# try:
#     numarator = int(input("Enter numarator: "))
#     numitor = int(input("Enter numitor: "))
#     result = numarator / numitor
#     print(result)
# except Exception:
#     print("Something went wrong!")
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print("You're trying to divide a number to a data type that cannot be divided with a number!")
# else:
#     print(result)
# finally:
#     print("Mereu se va executa")

# ZeroDivisionError
# try:
#     result = 5 / 0
# except ZeroDivisionError as e:
#     print(e)

# ValueError
# try:
#     result = 5 / int("mama")
# except ValueError as e:
#     print("You're trying to divide a number to a data type that cannot be divided with a number!")

# TypeError
# try:
#     result = "10" + 5
# except TypeError:
#     print("Type Error!")

# NameError
# try:
#     print(variable)
# except NameError:
#     print("We don't have such a variable!")

# FileNotFoundError
# try:
#     file = open("doesntexist.txt", "r")
# except FileNotFoundError:
#     print("This specified path file doesn't exist")

# IndexError
# try:
#     lst = [1, 2, 3, 4]
#     print(lst[5])
# except IndexError:
#     print("List index is out of bounds!")

# KeyError
# try:
#     my_dict = {"key": "value"}
#     print(my_dict["badkey"])
# except KeyError:
#     print("Specified key hasn't been found in the dictionary!")

# AttributeError
try:
    lst = [1, 2, 3]
    lst.append(4)
    lst.length
except AttributeError:
    print("Such an attribute doesn't exist for your class!")
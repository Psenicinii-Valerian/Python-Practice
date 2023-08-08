import os
import shutil

# file open modes: "w" - write, "a" - append, "r" - read

                                            # Reading files
# # 1) reading from outside
# path = "C:\\Users\\Valerian\\OneDrive\\Desktop\\STEP IT\\Python\\Lectia 4\\fisier.txt"
# file = open(path, "r")
# content = file.read()
# print(content)
# file.close()
#
# # 2) reading from project itself
# file = open("text.txt", "r")
# content = file.read()
# print(content)
# file.close()
#
#                                             # Creating file
# # with operator - automatizeaza lucrul cu fisiere; nu este necesar sa folosim file.close()
# with open("style.css", "w") as file:
#     file.write("Python seara vinerea dupa o zi de lucru este plictisitor")
#
# with open("style.css", "r") as file:
#     print(file.read())
#
# with open("index.html", "w") as file:
#     file.write('<h1 style="color: crimson;">Salut, mama</h1>')
#
# # Appending text to the file - write continuously the info, without deleting previous file info
# with open("another_text.txt", "w") as file:
#     file.write("Primul text\n")
#
# with open("another_text.txt", "a") as file:
#     file.write("Al doilea text")


                                            # Folders
# # Creating a folder
# folder_name = "Papka"
# os.mkdir(folder_name)

# # how to create a file in a folder
# folder_name = "Papocika"
# os.mkdir(folder_name)
#
# # os.path.join(path, "file.ext") - joins arguments into a path (as a string of a path)
# file_path = os.path.join(folder_name, "new.txt")
# with open(file_path, "w") as file:
#     file.write("Fisier in folder")
# with open(file_path, "r") as file:
#     print(file.read())

# # counting words in a file
# with open("words.txt", "w") as file:
#     file.write("Mama are dorinta sa cumpere un Bugatti")
# file = open("words.txt", "r")
# content = file.read()
# words = content.split(" ")
# words_len = len(words)
# print(f"Tu ai {words_len} cuvinte in fisier")
# file.close()

# # how to copy a file
# with open("new.txt", "w") as file:
#     file.write("Pasha Technik top")
#
# source_file = open("new.txt", "r")
# destination_file = open("test.txt", "w")
#
# content = source_file.read()
# destination_file.write(content)
#
# source_file.close()
# destination_file.close()

# # Project
#     # Folder
#         # 3 .html
#         # 2 .css
#         # 9 .txt
#
# def find_files_by_ext(folder_path, ext):
#     file_list = []
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith(ext):
#                 file_path = os.path.join(root, file)
#                 file_list.append(file_path)
#     return file_list
#
# folder_path = "C:\\Users\\Valerian\\OneDrive\\Desktop\\STEP IT\\Python\\Lectia 4\\Lucrul cu fisiere\\Folder"
# ext = ".txt"
# files = find_files_by_ext(folder_path, ext)
# print("Here are your files:")
# for file in files:
#     print(file)


                                                # how to copy a file normally
# with open("file.txt", "w") as file:
#     file.write("I love programming and it loves me")
#
# shutil.copy("file.txt", "copy.txt")

# source = "C:\\Users\\Valerian\\OneDrive\\Desktop\\STEP IT\\Python\\Lectia 4\\Lucrul cu fisiere\\copy.txt"
# dest = "C:\\Users\\Valerian\\OneDrive\\Desktop\\STEP IT\\Python\\Lectia 4\\Lucrul cu fisiere\\Copy Text\\copy.txt"
#
# if os.path.exists(dest):
#     print("The specified copy.txt file already exists in the specified destination")
# else:
#     os.replace(source, dest)
#     print("File replaced successfully")

                                                    # remove a file
# to_remove = "new.txt"
# if os.path.exists(to_remove):
#     os.remove(to_remove)
#     print("The specified file has been removed!")
# else:
#     print("File to remove doesn't exist at the specified path!")

# # 1) scriem o functie care schimba un cuvant pe altul dintr-un fisier
# def change_word_in_a_file():
#     with open("ex1.txt", "w") as file:
#         file.write("hello ")
#         file.write("world ")
#         file.write("football ")
#         file.write("Charles de Gaule")
#
#     with open("ex1.txt", "r") as file:
#         content = file.read()
#         word_list = content.split(" ")
#         print(word_list)
#
#         print("What word from here do you want to change: ")
#         i = 1
#
#         for word in word_list:
#             print(f"{i}) {word}")
#             i += 1
#
#         option = input("Enter the word you want to change: ")
#
#     with open("ex1.txt", "w") as file:
#         for word in word_list:
#             if word == option:
#                 word = input(f"Enter the word you want to insert instead of {option}: ")
#                 found = True
#             file.write(word + " ")
#         if found != True:
#             print("The specified word hasn't been found in the file!")
#         else:
#             print("Chanes saved successfully!")
#
# # 2) scriem o functie care sterge un cuvant din fisier
# def delete_word_in_a_file():
#     with open("ex2.txt", "w") as file:
#         file.write("programming ")
#         file.write("IT ")
#         file.write("computer ")
#         file.write("Bill Gates")
#
#     with open("ex2.txt", "r") as file:
#         content = file.read()
#         word_list = content.split(" ")
#         print(word_list)
#
#         print("What word from here do you want to delete: ")
#         i = 1
#
#         for word in word_list:
#             print(f"{i}) {word}")
#             i += 1
#
#         option = input("Enter the word you want to delete: ")
#
#     with open("ex2.txt", "w") as file:
#         for word in word_list:
#             if word == option:
#                 word = " "
#                 found = True
#             file.write(f'{"" if word == " " else word + " "}')
#         if found != True:
#             print("The specified word hasn't been found in the file!")
#         else:
#             print("Chanes saved successfully!")
# # main
# # change_word_in_a_file()
# delete_word_in_a_file()

                                        # Another variant to solve this tasks:
# 1)Scriem o functie care schimba un cuvint pe altul dintrun fisier
#Din Mama are mere => Mama are rosii

def f1(fisier, old, new):
    with open(fisier, 'r') as file:
        text = file.read()
        text_nou = text.replace(old, new)

    with open(fisier, 'w') as file:
        file.write(text_nou)

fisier = 'exemplu1.txt'
old = 'mere'
new = 'rosii'
f1(fisier, old, new)

#2)Scrie o functie care sterge un cuvint din fisier
#Din Mama are rosii => Mama are
def f2(fisier, del_word):
    with open(fisier, 'r') as file:
        text = file.read()
        text_nou = text.replace(del_word, "")
    with open(fisier, 'w') as file:
        file.write(text_nou)

fisier = 'exemplu2.txt'
del_word = 'rosii'
f2(fisier, del_word)

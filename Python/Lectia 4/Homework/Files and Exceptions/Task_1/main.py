# exercise 1
def create_file():
    choice = input("Do you want to create a new file with data? (Yes/No): ")
    if choice == "Yes" or choice == "Y" or choice == "yes" or choice == "y":
        choice = True
    else:
        choice = False

    if choice:
        file_name = input("Enter file name and it's extension: ")
        with open(file_name, "w") as file:
            text_to_file = []
            while True:
                text = input("Enter any text to save in the file ('end!' to stop): ")
                if text != "end!":
                    text_to_file.append(text)
                else:
                    break
            for txt in text_to_file:
                file.write(txt)
                file.write("\n")


def copy_from_file_to_another(output_file_name, input_file_name):
    text = ""
    try:
        with open(output_file_name, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File to read the data from not found! Try again after creating one.")
        exit(0)

    with open(input_file_name, "w") as file:
        file.write(text)


# main
create_file()
output_file_name = input("Enter the name of the file from which you want to read data: ")
input_file_name = input("Enter the name of the file in which you want to store data: ")
copy_from_file_to_another(output_file_name, input_file_name)

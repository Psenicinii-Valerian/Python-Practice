# exercise 3
def insert_data_into_file():
    file_name = input("Enter file name and it's extension (to write data into it): ")
    with open(file_name, "w") as file:
        text_to_file = []
        while True:
            option = input("Enter any mathematical operations, the result will be saved automatically in the file, 'end!' to stop: ")
            if option != "end!":
                result = 0

                while True:
                    try:
                        num1 = int(input("Enter first number: "))
                        num2 = int(input("Enter second number: "))
                        break
                    except ValueError:
                        print("Invalid data type inserted!")
                    except TypeError:
                        print("Type Error!")

                print("+. Addition")
                print("-. Substraction")
                print("*. Multiplication")
                print("/. Division")

                operation = input("Enter the operation: ")
                if operation == '+':
                    result = num1 + num2
                    file.write(str(result) + "\n")

                elif operation == '-':
                    result = num1 - num2
                    file.write(str(result) + "\n")

                elif operation == '*':
                    result = num1 * num2
                    file.write(str(result) + "\n")

                elif operation == '/':
                    try:
                        result = num1 / num2
                        file.write(str(result) + "\n")
                    except ZeroDivisionError:
                        print("You cannot divide a number by 0!")

                else:
                    print("Wrong input! Try again")
            else:
                break
    return file_name


def show_results_from_file(output_file_name):
    text = ""
    try:
        with open(output_file_name, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("File to read the data from not found! Try again after creating one.")
        exit(0)

    results = text.split("\n")
    i = 1

    print("Results:")
    for result in results:
        if result != "":
            print(f"{i}. {result}")
            i += 1


# main
output_file_name = insert_data_into_file()
show_results_from_file(output_file_name)

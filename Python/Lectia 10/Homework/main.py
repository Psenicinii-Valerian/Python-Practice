                                                            # Exercise 1
# def get_mobile_media(input_data):
#     s = 0
#     res = 0
#     output_data = list(zip(input_data, [(s := (s + x)) and (res := s/(index+1)) for index, x in enumerate(input_data)]))
#     print("Formed Zip Pairs:")
#     print(output_data)
#     in_data, mobile_media = zip(*output_data)
#     return list(mobile_media)
#
# print("Exercise 1:")
# input_data = [1, 2, 3, 4, 5]
# mobile_media = get_mobile_media(input_data)
# print("Final Result:")
# print(mobile_media)
# print()


                                                          # Exercise 2
# def extract_lines_from_matrix(matrix, lines):
#     output_data = list(zip(matrix, [i for index, i in enumerate(matrix) if index in lines]))
#     in_data, matrix_lines = zip(*output_data)
#     return list(matrix_lines)
#
# print("Exercise 2:")
# lines = []
# matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# available_lines = []
# for index, i in enumerate(matrix):
#     available_lines.append(index)
#
# print("Initial matrix:", matrix)
#
# while True:
#     try:
#         line = int(input("Enter the lines index that you want to extract from matrix (x to stop): "))
#         if line in available_lines:
#             lines.append(line)
#         else:
#             print("Cannot acces an inexistent matrix line index!")
#     except Exception:
#         break
#
# matrix_lines = extract_lines_from_matrix(matrix, lines)
# print(matrix_lines)


                                                         # Exercise 3
# def fibonacci_numbers(p):
#     fibonacci_series = []
#     for i in range(2):
#         fibonacci_series.append(i)
#
#     for fibonacci_index, i in enumerate(range(2, p)):
#         fibonacci_index = fibonacci_index + 2
#         next_num = fibonacci_series[fibonacci_index-2] + fibonacci_series[fibonacci_index-1]
#         fibonacci_series.append(next_num)
#
#     return fibonacci_series
#
# print("Exercise 3:")
# number = int(input("Enter the number for which you want to do the Fibonacci series: "))
# fibonacci_series = fibonacci_numbers(number)
# print(fibonacci_series, "\n")


                                                        # Exercise 4
def is_prime(number):
    is_prime = True
    for i in range(2, number//2+1):
        if number % i == 0:
            is_prime = False
            break
    return is_prime

def is_prime_for_number(input_data):
    empty_keys = []
    my_dict = {number: list(filter(lambda x: number % x == 0 and is_prime(x), range(2, number//2+1))) for number in input_data}
    for index, value in my_dict.items():
        if len(value) == 0:
            empty_keys.append(index)

    for key in empty_keys:
        del my_dict[key]

    return my_dict

print("Exercise 4:")
input_data = [10, 15, 18, 21, 24, 28, 31]
my_dict = is_prime_for_number(input_data)
print(my_dict, "\n")


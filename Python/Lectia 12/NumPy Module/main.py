import numpy as np
                                                    # TASK 1
arr = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
res = arr - arr2
print("arr-arr2:", res)
print("arr[0]:", arr[0])
print()

                                                    # TASK 1
array = np.array([1, 2, 3])
summ = np.sum(array)
print("sum of the array:", summ)

matrix = np.array([[1, 2, 3], [4, 5, 7], [8, 9, 0]])
summ = np.sum(matrix)   # sum of elements
mean = np.mean(matrix)  # average number of a collection
mean = np.round(mean, decimals=2)
print("sum of the elements of the matrix:", summ)
print("mean value of the elements of the matrix:", mean)

max_index = np.argmax(matrix)  # index of maximum element
print("max_index:", max_index)
print()

sum_arr = arr + matrix
print("sum_arr:")
print(sum_arr)
print()

arr = np.array([1, 2, 3, 4, 5, 6])
print("arr:", arr)

# arr.reshape((randuri, coloane))
# daca dam -1 se va calcula automat parametrul la care dam aceasta valoare
# este necesar cel putin randul sau coloana sa fie valoare concreta - de la care ne vom orienta
# (al 2-lea parametru poate fi setat automat)
reshape_arr = arr.reshape((3, 2))
print("reshape_arr:")
print(reshape_arr)
print()

matrix = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
print("Matrix:")
print(matrix)
print()

reshape_matrix = matrix.reshape((matrix.size,))
print("reshape_matrix:")
print(reshape_matrix)

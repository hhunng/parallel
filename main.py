import random
from multiprocessing import Process, Array
from ctypes import c_int64
import random

def create_matrix(m, n, min_value=0, max_value=100):
    matrix = []
    for _ in range(m):
        row = [random.randint(min_value, max_value) for _ in range(n)]
        matrix.append(row)
    return matrix


def find_length(matrix, step, end, S):
    for i in range(step, end + 1):
        row_size = len(matrix[i])
        S[i] = row_size

def find_length_parallel(matrix):
    cpu = 4
    partition = int(len(matrix) / cpu)
    S = Array(c_int64, len(matrix))
    arr = []

    for process in range(cpu):
        step = process * partition
        end = step + partition - 1
        arr.append(Process(target=find_length, args=(matrix, step, end, S)))

    for process in range(cpu):
        arr[process].start()

    for process in range(cpu):
        arr[process].join()

    return [S[i] for i in range(len(matrix))]

        
if __name__ == "__main__":
    m = 1000
    n = 10000
    my_matrix = create_matrix(m, n, min_value=1, max_value=50)
    a = find_length_parallel(my_matrix)

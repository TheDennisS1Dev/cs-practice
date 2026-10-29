import numpy as np

def reshape_rows(values, width):
    if (len(values) == 0) or (len(values) % width != 0):
        return []
    else:
        array = np.array(values)
        count_rows = len(array) // width
        return np.round(array.reshape(count_rows, width), 6).tolist()

def block(matrix, rows, columns):
    if len(matrix) == 0:
        return []
    else:
        array = np.array(matrix)
        return np.round(array[np.ix_(rows, columns)], 6).tolist()

def column_means(matrix):
    if len(matrix) == 0:
        return 0.0
    else:
        array = np.array(matrix)
        return np.round(np.mean(array, 0), 6).tolist()

def column_range(matrix, column):
    if len(matrix) == 0:
        return 0.0
    else:
        array = np.array(matrix)
        return np.round(np.max(array[:, column]) - np.min(array[:, column]), 6)

testarr = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print(block(testarr, [0, 2], [1, 2]))
print(column_means([[1, 2], [3, 4], [5, 6]]))
print(column_range([[1, 2], [5, 7]], 1))
print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))

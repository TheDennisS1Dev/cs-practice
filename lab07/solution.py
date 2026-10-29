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

print("test")

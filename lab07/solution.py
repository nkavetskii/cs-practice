import numpy as np


def reshape_rows(values, width):
    if not values or width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float)
    return arr.reshape(-1, width).tolist()

def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix):
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    return np.round(arr.mean(axis=0), 6).tolist()


def column_range(matrix, column):
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col = arr[:, column]
    return float(np.round(col.max() - col.min(), 6))



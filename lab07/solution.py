import numpy as np


def reshape_rows(values, width):
    if not values or width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float)
    return arr.reshape(-1, width).tolist()

def block(matrix, rows, columns):
    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()



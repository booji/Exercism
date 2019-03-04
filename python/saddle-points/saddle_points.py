import numpy as np

def saddle_points(matrix):
    if matrix == [] or matrix is None:
        return set()
    previous = None
    for item in matrix:
        if (previous is None):
            previous = len(item)
        elif previous != len(item):
            raise ValueError("Matrix shape irregular")

    matrix = np.asarray(matrix)
    max_in_row =np.asarray(matrix.max(axis=1,keepdims=True) == matrix)
    min_in_column = np.asarray(matrix.min(axis=0, keepdims=True) == matrix)

    #combine mask only if both states are true is it a 'saddle position'
    mask = np.logical_and(max_in_row, min_in_column)
    #indexing starts at 1 for expected result
    indecies = np.argwhere(mask == True) + 1

    return set(list(map(tuple,indecies)))

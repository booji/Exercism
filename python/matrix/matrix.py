import numpy as np

#Using numpy assuming that more math operations would be included
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = np.array(
            [m.split(" ") for m in matrix_string.split('\n')],
            dtype=np.int32)

    def row(self, index):
        return self.matrix[index - 1, :].tolist()

    def column(self, index):
        return self.matrix[:, index - 1].tolist()

import numpy as np
def square_of_sum(count):
    return np.power(sum(range(1,count+1)),2)


def sum_of_squares(count):
    return np.power(range(1,count+1),2).sum()


def difference(count):
    return square_of_sum(count)-sum_of_squares(count)

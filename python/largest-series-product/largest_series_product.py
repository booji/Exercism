from functools import reduce
def largest_product(series, size):
    if size == 0:
        return 1
    if not series:
        raise ValueError("Series empty")
    if len(series) < size:
        raise ValueError("Series length to small for size.")
    if size < 0:
        raise ValueError("Size has to be postivie Integer.")
    digits = [series[i:i+size] for i in range(len(series)-size+1)]
    maxVal = 0
    for section in digits:
        testVal = reduce(lambda x, y: int(x)*int(y), list(section))
        if testVal > maxVal:
            maxVal = testVal
    return maxVal

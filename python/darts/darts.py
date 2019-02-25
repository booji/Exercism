def score(x, y):
    score = 0
    if (x or y) > 10:
        return score
    point = x**2+y**2

    if point <= 100:
        score = 1
    if point <= 25:
        score = 5
    if point <= 1:
        score = 10
    return score

def is_triangle(sides):
    if min(sides) <= 0 or sum(sorted(sides)[:-1]) < max(sides) or len(sides) != 3:
        return False
    return True

def is_equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides)


def is_isosceles(sides):
    return len(set(sides)) < 3 and is_triangle(sides)


def is_scalene(sides):
    return len(set(sides)) == 3 and is_triangle(sides)

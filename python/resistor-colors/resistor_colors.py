from collections import defaultdict
BAND_COLORS = defaultdict(None, {"black": 0,
               "brown": 1,
               "red": 2,
               "orange": 3,
               "yellow": 4,
               "green": 5,
               "blue": 6,
               "violet": 7,
               "grey": 8,
               "white": 9})


def value(colors):
    if len(colors) != 2:
        raise ValueError("Only two colour bands on this resistor calc.")
    colors = [color.lower() for color in colors]

    result = ""
    # print(colors)
    for color in colors:
        result += str(BAND_COLORS.get(color, "E"))
    if 'E' in result:
        raise ValueError(f"Invalid colour band chosen: {result}")

    return int(result)

def raindrops(number):
    factor_string = [(3, "Pling"),
                     (5, "Plang"),
                     (7, "Plong")]

    result = [sound for factor, sound in factor_string
              if number % factor == 0]

    if result == []:
        result.append(str(number))

    return "".join(result)

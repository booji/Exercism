def sum_of_multiples(limit, multiples):
    result = set()
    try:
        multiples.remove(0)
    except:
        pass
    for number in range(1,limit):
        result.update([number for factor in multiples
                  if number % factor == 0])
    return sum(result)

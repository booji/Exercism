import math
def prime_factors(natural_number):
    factors = []

    i = 2
    # Find all prime '2' the remainder will be odd.
    while natural_number%i == 0:
        natural_number = natural_number // i
        factors.append(i)

    # Go up to sqrt(natural_number) as prime*prime cannot be greater then
    # natural_number. Increment by 2 as no more even number remaining
    for i in range(3,int(math.sqrt(natural_number))+1,2):
        while natural_number%i == 0:
            natural_number = natural_number // i
            factors.append(i)
            
    # add last value which will be prime if greater than 2
    if natural_number > 2:
        factors.append(natural_number)
    return factors
